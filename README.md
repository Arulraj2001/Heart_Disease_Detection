# Heart Disease Prediction and Analysis

## Overview
This is a Django-based web application for predicting heart disease and analyzing related data. Users can input their medical details to predict the likelihood of heart disease using a trained machine learning model. The application also allows for dataset uploads to retrain the model with new data.

## Features
- **Heart Disease Prediction**: Users can input medical parameters to get a prediction.
- **Data Visualizations**: Graphs and charts to understand heart disease distribution.
- **Upload Dataset**: Allows uploading new datasets to retrain the model.
- **Informational Pages**: About, Contact, Do’s and Don’ts, and Doctor Consultation pages.

## Tech Stack
- **Backend**: Django, Scikit-learn, Pandas, NumPy
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: CSV file-based dataset handling

## Installation Guide
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Required Python libraries

### Setup
1. Clone the repository:
   ```bash
   git clone ""
   cd heart-disease-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Django migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```
5. Open your browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
- Navigate to the **Prediction Page** and enter required details.
- Check **Visualizations** for insights on the dataset.
- Use the **Upload Dataset** page to upload a new dataset and retrain the model.

## Project Structure
```
heart_app/
│── migrations/        # Django database migrations
│── templates/         # HTML files
│── static/            # CSS, JavaScript, and assets
│── views.py           # Handles app logic
│── urls.py            # Defines URL routing
│── models.py          # Database models
│── forms.py           # Forms for user input
│── heart_disease_data.csv  # Default dataset
manage.py              # Django project manager
```

## Dataset Format
The dataset should be in CSV format with the following columns:
```
age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target
```

## Contribution
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

