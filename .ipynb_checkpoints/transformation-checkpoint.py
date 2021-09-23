{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f9e1f834",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "DataFrame constructor not properly called!",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-10-b84582e7c93e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     16\u001b[0m \u001b[0mextract_data_file\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"Extract_data.csv\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 18\u001b[1;33m \u001b[0mextract_data_df\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mextract_data_file\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     19\u001b[0m \u001b[0mextract_data_df\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhead\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\core\\frame.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, data, index, columns, dtype, copy)\u001b[0m\n\u001b[0;32m    588\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    589\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mindex\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0mcolumns\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 590\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"DataFrame constructor not properly called!\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    591\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    592\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mdtype\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: DataFrame constructor not properly called!"
     ]
    }
   ],
   "source": [
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests\n",
    "import time\n",
    "from scipy.stats import linregress\n",
    "\n",
    "# # Import API key\n",
    "# from my_keys import weather_api_key\n",
    "\n",
    "# # Incorporated citipy to determine city based on latitude and longitude\n",
    "# from citipy import citipy\n",
    "\n",
    "# Output File (CSV)\n",
    "extract_data_file = \"Extract_data.csv\"\n",
    "\n",
    "extract_data_df = pd.DataFrame(extract_data_file)\n",
    "extract_data_df.head(5)\n"
   ]
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
