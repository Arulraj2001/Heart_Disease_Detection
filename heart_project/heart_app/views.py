import numpy as np
import pandas as pd
from django.shortcuts import render
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from django.core.files.storage import FileSystemStorage

# Load dataset
DATA_PATH = 'heart_app/heart_disease_data.csv'
heart_data = pd.read_csv(DATA_PATH)

# Prepare the data for training
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the scaled data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the Logistic Regression model with higher iterations
model = LogisticRegression(max_iter=200)
model.fit(X_train, Y_train)

# Views
def home(request):
    """Renders the home page."""
    return render(request, 'heart_app/home.html')

def visualizations(request):
    target_counts = heart_data['target'].value_counts().to_dict()
    age_distribution = heart_data['age'].tolist()

    data = {
        'target_labels': list(target_counts.keys()),
        'target_values': list(target_counts.values()),
        'age_distribution': age_distribution,
    }
    return render(request, 'heart_app/visualizations.html', {'data': data})


def predict(request):
    if request.method == 'POST':
        try:
            # Get user input
            input_data = [
                float(request.POST['age']),
                float(request.POST['sex']),
                float(request.POST['cp']),
                float(request.POST['trestbps']),
                float(request.POST['chol']),
                float(request.POST['fbs']),
                float(request.POST['restecg']),
                float(request.POST['thalach']),
                float(request.POST['exang']),
                float(request.POST['oldpeak']),
                float(request.POST['slope']),
                float(request.POST['ca']),
                float(request.POST['thal']),
            ]

            # Convert input to numpy array and predict
            input_data_np = np.asarray(input_data).reshape(1, -1)
            prediction = model.predict(input_data_np)

            # Render result
            if prediction[0] == 1:
                result = 'Heart Disease Detected'
            else:
                result = 'No Heart Disease Detected'

        except Exception as e:
            result = f"Error in processing input: {str(e)}"

        return render(request, 'heart_app/predict.html', {'result': result})

    return render(request, 'heart_app/predict.html')

def about(request):
    """Renders the about page."""
    return render(request, 'heart_app/about.html')

def contact(request):
    """Renders the contact page."""
    return render(request, 'heart_app/contact.html')

def doctor(request):
    """Renders the doctor page."""
    return render(request, 'heart_app/doctor.html')

def dodont(request):
    """Renders the doctor page."""
    return render(request, 'heart_app/dodont.html')

def upload_dataset(request):
    if request.method == 'POST' and request.FILES['dataset']:
        dataset_file = request.FILES['dataset']
        fs = FileSystemStorage()
        file_path = fs.save(dataset_file.name, dataset_file)
        file_url = fs.url(file_path)

        # Load and validate dataset
        try:
            new_data = pd.read_csv(fs.path(file_path))
            required_columns = list(heart_data.columns)
            if all(column in new_data.columns for column in required_columns):
                global model, X, Y
                X = new_data.drop(columns='target', axis=1)
                Y = new_data['target']
                model.fit(X, Y)
                messages.success(request, 'Dataset uploaded and model retrained successfully!')
            else:
                messages.error(request, 'Dataset does not match the required format.')
        except Exception as e:
            messages.error(request, f'Error processing the dataset: {str(e)}')

        return render(request, 'heart_app/upload.html', {'file_url': file_url})

    return render(request, 'heart_app/upload.html')