{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import svm\n",
    "from sklearn.metrics import accuracy_score\n",
    "import pickle\n",
    "import streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# loading the diabetes dataset to a pandas DataFrame\n",
    "diabetes_dataset = pd.read_csv('/Users/hesham/Desktop/diabetes.csv') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6</td>\n",
       "      <td>148</td>\n",
       "      <td>72</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.627</td>\n",
       "      <td>50</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>66</td>\n",
       "      <td>29</td>\n",
       "      <td>0</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.351</td>\n",
       "      <td>31</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>183</td>\n",
       "      <td>64</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>23.3</td>\n",
       "      <td>0.672</td>\n",
       "      <td>32</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>89</td>\n",
       "      <td>66</td>\n",
       "      <td>23</td>\n",
       "      <td>94</td>\n",
       "      <td>28.1</td>\n",
       "      <td>0.167</td>\n",
       "      <td>21</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>137</td>\n",
       "      <td>40</td>\n",
       "      <td>35</td>\n",
       "      <td>168</td>\n",
       "      <td>43.1</td>\n",
       "      <td>2.288</td>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0            6      148             72             35        0  33.6   \n",
       "1            1       85             66             29        0  26.6   \n",
       "2            8      183             64              0        0  23.3   \n",
       "3            1       89             66             23       94  28.1   \n",
       "4            0      137             40             35      168  43.1   \n",
       "\n",
       "   DiabetesPedigreeFunction  Age  Outcome  \n",
       "0                     0.627   50        1  \n",
       "1                     0.351   31        0  \n",
       "2                     0.672   32        1  \n",
       "3                     0.167   21        0  \n",
       "4                     2.288   33        1  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# printing the first 5 rows of the dataset\n",
    "diabetes_dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(768, 9)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# number of rows and Columns in this dataset\n",
    "diabetes_dataset.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.845052</td>\n",
       "      <td>120.894531</td>\n",
       "      <td>69.105469</td>\n",
       "      <td>20.536458</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>31.992578</td>\n",
       "      <td>0.471876</td>\n",
       "      <td>33.240885</td>\n",
       "      <td>0.348958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3.369578</td>\n",
       "      <td>31.972618</td>\n",
       "      <td>19.355807</td>\n",
       "      <td>15.952218</td>\n",
       "      <td>115.244002</td>\n",
       "      <td>7.884160</td>\n",
       "      <td>0.331329</td>\n",
       "      <td>11.760232</td>\n",
       "      <td>0.476951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.078000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>27.300000</td>\n",
       "      <td>0.243750</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>117.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>30.500000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0.372500</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>140.250000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>127.250000</td>\n",
       "      <td>36.600000</td>\n",
       "      <td>0.626250</td>\n",
       "      <td>41.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>17.000000</td>\n",
       "      <td>199.000000</td>\n",
       "      <td>122.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>846.000000</td>\n",
       "      <td>67.100000</td>\n",
       "      <td>2.420000</td>\n",
       "      <td>81.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Pregnancies     Glucose  BloodPressure  SkinThickness     Insulin  \\\n",
       "count   768.000000  768.000000     768.000000     768.000000  768.000000   \n",
       "mean      3.845052  120.894531      69.105469      20.536458   79.799479   \n",
       "std       3.369578   31.972618      19.355807      15.952218  115.244002   \n",
       "min       0.000000    0.000000       0.000000       0.000000    0.000000   \n",
       "25%       1.000000   99.000000      62.000000       0.000000    0.000000   \n",
       "50%       3.000000  117.000000      72.000000      23.000000   30.500000   \n",
       "75%       6.000000  140.250000      80.000000      32.000000  127.250000   \n",
       "max      17.000000  199.000000     122.000000      99.000000  846.000000   \n",
       "\n",
       "              BMI  DiabetesPedigreeFunction         Age     Outcome  \n",
       "count  768.000000                768.000000  768.000000  768.000000  \n",
       "mean    31.992578                  0.471876   33.240885    0.348958  \n",
       "std      7.884160                  0.331329   11.760232    0.476951  \n",
       "min      0.000000                  0.078000   21.000000    0.000000  \n",
       "25%     27.300000                  0.243750   24.000000    0.000000  \n",
       "50%     32.000000                  0.372500   29.000000    0.000000  \n",
       "75%     36.600000                  0.626250   41.000000    1.000000  \n",
       "max     67.100000                  2.420000   81.000000    1.000000  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# getting the statistical measures of the data\n",
    "diabetes_dataset.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    500\n",
       "1    268\n",
       "Name: Outcome, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "diabetes_dataset['Outcome'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# separating the data and labels\n",
    "X = diabetes_dataset.drop(columns = 'Outcome', axis=1)\n",
    "Y = diabetes_dataset['Outcome']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(768, 8) (614, 8) (154, 8)\n"
     ]
    }
   ],
   "source": [
    "print(X.shape, X_train.shape, X_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "classifier = svm.SVC(kernel='linear')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SVC(kernel='linear')"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#training the support vector Machine Classifier\n",
    "classifier.fit(X_train, Y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# accuracy score on the training data\n",
    "X_train_prediction = classifier.predict(X_train)\n",
    "training_data_accuracy = accuracy_score(X_train_prediction, Y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy score of the training data :  0.7833876221498371\n"
     ]
    }
   ],
   "source": [
    "print('Accuracy score of the training data : ', training_data_accuracy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# accuracy score on the test data\n",
    "X_test_prediction = classifier.predict(X_test)\n",
    "test_data_accuracy = accuracy_score(X_test_prediction, Y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy score of the test data :  0.7727272727272727\n"
     ]
    }
   ],
   "source": [
    "print('Accuracy score of the test data : ', test_data_accuracy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n",
      "The person is diabetic\n"
     ]
    }
   ],
   "source": [
    "input_data = (5,166,72,19,175,25.8,0.587,51)\n",
    "\n",
    "# changing the input_data to numpy array\n",
    "input_data_as_numpy_array = np.asarray(input_data)\n",
    "\n",
    "# reshape the array as we are predicting for one instance\n",
    "input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
    "\n",
    "prediction = classifier.predict(input_data_reshaped)\n",
    "print(prediction)\n",
    "\n",
    "if (prediction[0] == 0):\n",
    "  print('The person is not diabetic')\n",
    "else:\n",
    "  print('The person is diabetic')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "filename = 'trained_model.sav'\n",
    "pickle.dump(classifier, open(filename, 'wb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# loading the saved model\n",
    "loaded_model = pickle.load(open('trained_model.sav', 'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n",
      "The person is diabetic\n"
     ]
    }
   ],
   "source": [
    "input_data = (5,166,72,19,175,25.8,0.587,51)\n",
    "\n",
    "# changing the input_data to numpy array\n",
    "input_data_as_numpy_array = np.asarray(input_data)\n",
    "\n",
    "# reshape the array as we are predicting for one instance\n",
    "input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
    "\n",
    "prediction = loaded_model.predict(input_data_reshaped)\n",
    "print(prediction)\n",
    "\n",
    "if (prediction[0] == 0):\n",
    "  print('The person is not diabetic')\n",
    "else:\n",
    "  print('The person is diabetic')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "# creating a function for Prediction\n",
    "\n",
    "def diabetes_prediction(input_data):\n",
    "    \n",
    "\n",
    "    # changing the input_data to numpy array\n",
    "    input_data_as_numpy_array = np.asarray(input_data)\n",
    "\n",
    "    # reshape the array as we are predicting for one instance\n",
    "    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
    "\n",
    "    prediction = loaded_model.predict(input_data_reshaped)\n",
    "    print(prediction)\n",
    "\n",
    "    if (prediction[0] == 0):\n",
    "      return 'The person is not diabetic'\n",
    "    else:\n",
    "      return 'The person is diabetic'\n",
    "  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    \n",
    "    \n",
    "    # giving a title\n",
    "    st.title('Diabetes Prediction Web App')\n",
    "    \n",
    "    \n",
    "    # getting the input data from the user\n",
    "    \n",
    "    \n",
    "    Pregnancies = st.text_input('Number of Pregnancies')\n",
    "    Glucose = st.text_input('Glucose Level')\n",
    "    BloodPressure = st.text_input('Blood Pressure value')\n",
    "    SkinThickness = st.text_input('Skin Thickness value')\n",
    "    Insulin = st.text_input('Insulin Level')\n",
    "    BMI = st.text_input('BMI value')\n",
    "    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')\n",
    "    Age = st.text_input('Age of the Person')\n",
    "    \n",
    "    \n",
    "    # code for Prediction\n",
    "    diagnosis = ''\n",
    "    \n",
    "    # creating a button for Prediction\n",
    "    \n",
    "    if st.button('Diabetes Test Result'):\n",
    "        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])\n",
    "        \n",
    "        \n",
    "    st.success(diagnosis)\n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
