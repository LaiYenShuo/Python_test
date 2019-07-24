{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    " def count_NA(data):\n",
    "        tmp = []\n",
    "        result = []\n",
    "        for i in range(0,data.shape[1]):\n",
    "            if i == 0:\n",
    "                result = data.iloc[:,i].isna().value_counts()\n",
    "            else:\n",
    "                tmp = data.iloc[:,i].isna().value_counts()\n",
    "                result = pd.concat([result, tmp], axis = 1)\n",
    "        result = result.fillna('0')\n",
    "        result.index = ['non_NA_count', 'NA_count']\n",
    "        return result"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
