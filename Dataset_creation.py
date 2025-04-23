{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "105e692c-5371-4f9d-bc49-bcdeee21e034",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "314b8516-4664-47fd-b57b-6a50693cefb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the list of categories\n",
    "categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "19879a30-fe34-4163-bd00-daa667d978c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Number of entries (n)\n",
    "n = 90000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5f9022b0-90e0-414a-a360-0a15ce850788",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate random data\n",
    "data = {\n",
    "    'Date': pd.date_range('2015-01-01','2023-12-31', periods=n),\n",
    "    'Category': [random.choice(categories) for _ in range(n)],\n",
    "    'Likes': np.random.randint(0, 10000, size=n),\n",
    "    'Shares': np.random.randint(0, 1000, size=n),\n",
    "    'Reposts': np.random.randint(0, 200, size=n),\n",
    "    'Comments': np.random.randint(0, 10000, size=n)\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8af8ac5d-b8c3-45be-9338-7507ff4eaced",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a DataFrame\n",
    "df = pd.DataFrame(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ae5db4d2-d2ae-4395-a3c8-43115fbe67bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Split the 'Date' column into separate 'Date' and 'Time' columns\n",
    "df['Date'] = df['Date'].dt.date  # Extract only the date component"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "80a23ece-6c58-4cdc-8fbc-aec54f9a1bd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('Twitter_Analysis.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3e73c665-7093-44d8-a96a-66ba4874445d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date Category  Likes  Shares  Reposts  Comments\n",
      "0  2015-01-01  Culture   3457     815      193      7965\n",
      "1  2015-01-01   Health    348      32      163      7740\n",
      "2  2015-01-01   Health   3450     119       60      6723\n",
      "3  2015-01-01   Health   9678     129        5      5255\n",
      "4  2015-01-01     Food   5195     633      129      9021\n",
      "5  2015-01-01     Food   4993     741      152      4245\n",
      "6  2015-01-01    Music   9196      50      139      7570\n",
      "7  2015-01-01    Music    881     615      163       751\n",
      "8  2015-01-01   Travel   2508     289       37      4133\n",
      "9  2015-01-01   Health   2456     862       20      4744\n"
     ]
    }
   ],
   "source": [
    "# Print the first few rows of the DataFrame\n",
    "print(df.head(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7d0f256-85f1-4e0c-8534-14e2c2d8aa49",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
