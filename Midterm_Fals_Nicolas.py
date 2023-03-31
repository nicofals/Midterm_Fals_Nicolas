#!/usr/bin/env python
# coding: utf-8

# In[1]:


#histogram, slide 2
import json
import matplotlib.pyplot as plt
with open('numbers.txt', 'r') as f:
    numbers = f.read().splitlines()
    numbers = [num.split(',') for num in numbers]
    numbers = [int(num) for sublist in numbers for num in sublist]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
for num, freq in frequency.items():
    print(f'{num}: {freq}')
plt.hist(numbers, bins=max(numbers)-min(numbers)+1, rwidth=0.8)
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Number Frequency Histogram')
plt.show()
with open('frequency.json', 'w') as f:
    json.dump(frequency, f)


# In[2]:


#Slide 3
import matplotlib.pyplot as plt
prices = {
    "April": 10,
    "May": 18,
    "June": 6,
    "July": 26
}
labels = prices.keys()
sizes = prices.values()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title("Frequencies of Purchases in Different Months")
plt.show()


# In[3]:


#Slide 4
import matplotlib.pyplot as plt
from collections import Counter
dates = ['4/1/19', '4/1/19', '4/4/19', '4/5/19', '4/5/19', '4/7/19', '4/8/19', '4/20/19', '4/23/19',
         '5/5/19', '5/6/19', '5/10/19', '5/14/19', '5/18/19', '5/19/19', '5/21/19', '5/21/19', '5/21/19',
         '5/22/19', '5/22/19', '5/22/19', '5/24/19', '5/25/19', '5/28/19', '5/29/19', '5/30/19', '5/30/19',
         '6/3/19', '6/3/19', '6/5/19', '6/18/19', '6/25/19', '6/25/19', '7/3/19', '7/3/19', '7/3/19',
         '7/3/19', '7/3/19', '7/6/19', '7/6/19', '7/6/19', '7/6/19', '7/6/19', '7/7/19', '7/9/19', '7/17/19',
         '7/18/19', '7/18/19', '7/18/19', '7/18/19', '7/21/19', '7/21/19', '7/23/19', '7/30/19', '7/30/19',
         '7/30/19', '7/31/19', '7/31/19']
freq = Counter(dates)
sorted_dates = sorted(freq.items())
x_values = [i for i in range(len(sorted_dates))]
y_values = [date[1] for date in sorted_dates]
plt.bar(x_values, y_values)
plt.xticks(x_values, [date[0] for date in sorted_dates], rotation=90)
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.title('Order Dates')
plt.show()


# In[4]:


#Slide 5
import pandas as pd
import matplotlib.pyplot as plt
order_dates = ['4/1/19', '4/1/19', '4/4/19', '4/5/19', '4/5/19', '4/7/19', '4/8/19', '4/20/19', '4/23/19', '5/5/19', '5/6/19', '5/10/19', '5/14/19', '5/18/19', '5/19/19', '5/21/19', '5/21/19', '5/21/19', '5/22/19', '5/22/19', '5/22/19', '5/24/19', '5/25/19', '5/28/19', '5/29/19', '5/30/19', '5/30/19', '6/3/19', '6/3/19', '6/5/19', '6/18/19', '6/25/19', '6/25/19', '7/3/19', '7/3/19', '7/3/19', '7/3/19', '7/3/19', '7/6/19', '7/6/19', '7/6/19', '7/6/19', '7/6/19', '7/7/19', '7/9/19', '7/17/19', '7/18/19', '7/18/19', '7/18/19', '7/18/19', '7/21/19', '7/21/19', '7/23/19', '7/30/19', '7/30/19', '7/30/19', '7/31/19', '7/31/19']
df = pd.DataFrame({'order_date': order_dates})
df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%y')
df['month'] = df['order_date'].dt.month
freq = df['month'].value_counts()
freq.plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.show()


# In[5]:


#slide 6
import pandas as pd
import matplotlib.pyplot as plt
dates = pd.Series([
    '4/1/19', '4/1/19', '4/4/19', '4/5/19', '4/5/19', '4/7/19', '4/8/19', 
    '4/20/19', '4/23/19', '5/5/19', '5/6/19', '5/10/19', '5/14/19', '5/18/19', 
    '5/19/19', '5/21/19', '5/21/19', '5/21/19', '5/22/19', '5/22/19', '5/22/19', 
    '5/24/19', '5/25/19', '5/28/19', '5/29/19', '5/30/19', '5/30/19', '6/3/19', 
    '6/3/19', '6/5/19', '6/18/19', '6/25/19', '6/25/19', '7/3/19', '7/3/19', 
    '7/3/19', '7/3/19', '7/3/19', '7/6/19', '7/6/19', '7/6/19', '7/6/19', 
    '7/6/19', '7/7/19', '7/9/19', '7/17/19', '7/18/19', '7/18/19', '7/18/19', 
    '7/18/19', '7/21/19', '7/21/19', '7/23/19', '7/30/19', '7/30/19', '7/30/19', 
    '7/31/19', '7/31/19'
])
dates = pd.to_datetime(dates)
freq = dates.dt.to_period('M').value_counts().sort_index()
plt.plot(freq.index.strftime('%b'), freq.values)
plt.title('Frequency of Orders')
plt.xlabel('Month')
plt.ylabel('Frequency')
plt.show()


# In[6]:


#slide 7
import pandas as pd
import matplotlib.pyplot as plt
dates = pd.Series([
    '4/1/19', '4/1/19', '4/4/19', '4/5/19', '4/5/19', '4/7/19', '4/8/19', 
    '4/20/19', '4/23/19', '5/5/19', '5/6/19', '5/10/19', '5/14/19', '5/18/19', 
    '5/19/19', '5/21/19', '5/21/19', '5/21/19', '5/22/19', '5/22/19', '5/22/19', 
    '5/24/19', '5/25/19', '5/28/19', '5/29/19', '5/30/19', '5/30/19', '6/3/19', 
    '6/3/19', '6/5/19', '6/18/19', '6/25/19', '6/25/19', '7/3/19', '7/3/19', 
    '7/3/19', '7/3/19', '7/3/19', '7/6/19', '7/6/19', '7/6/19', '7/6/19', 
    '7/6/19', '7/7/19', '7/9/19', '7/17/19', '7/18/19', '7/18/19', '7/18/19', 
    '7/18/19', '7/21/19', '7/21/19', '7/23/19', '7/30/19', '7/30/19', '7/30/19', 
    '7/31/19', '7/31/19'
])
dates = pd.to_datetime(dates)
freq = dates.value_counts().sort_index()
plt.plot(freq.index, freq.values)
plt.title('Frequency of Orders')
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()


# In[7]:


#slide 8
import matplotlib.pyplot as plt
prices = [35.00, 16.99, 9.99, 147.98, 14.99, 11.99, 38.98, 44.99, 27.30, 37.08, 12.99, 7.20, 27.99, 15.32, 9.95, 38.89, 8.95, 12.99, 7.99, 16.98, 35.00, 7.50, 7.67, 9.80, 13.95, 9.99, 10.98, 32.98, 28.99, 13.88, 11.62, 11.98, 51.99, 10.59, 7.94, 8.32, 25.62, 0.52, 5.43, 12.99, 102.47, 79.97, 49.99, 199.99, 41.97, 15.60, 36.49, 15.95, 99.63, 12.78, 12.78, 6.49, 5.76, 42.93, 49.99, 6.30, 5.99, 35.99, 54.88]
total = sum(prices)
percentages = [(price/total)*100 for price in prices]
labels = ['${:.2f}'.format(price) for price in prices]
fig, ax = plt.subplots(figsize=(12,12))
ax.pie(percentages, labels=labels, autopct='%1.1f%%')
ax.set_title('Percentage of Prices')
plt.show()


# In[8]:


#slide 9
import matplotlib.pyplot as plt
prices = [35.00, 16.99, 9.99, 147.98, 14.99, 11.99, 38.98, 44.99, 27.30, 37.08,
          12.99, 7.20, 27.99, 15.32, 9.95, 38.89, 8.95, 12.99, 7.99, 16.98,
          35.00, 7.50, 7.67, 9.80, 13.95, 9.99, 10.98, 32.98, 28.99, 13.88,
          11.62, 11.98, 51.99, 10.59, 7.94, 8.32, 25.62, 0.52, 5.43, 12.99,
          102.47, 79.97, 49.99, 199.99, 41.97, 15.60, 36.49, 15.95, 99.63,
          12.78, 12.78, 6.49, 5.76, 42.93, 49.99, 6.30, 5.99, 35.99, 54.88]
above_100 = len([price for price in prices if price > 100])
between_50_and_100 = len([price for price in prices if 50 < price <= 100])
between_5_and_50 = len([price for price in prices if 5 < price <= 50])
total_prices = len(prices)
labels = ['$5 - $50', '$50 - $100', 'Above $100']
sizes = [between_5_and_50, between_50_and_100, above_100]
colors = ['#FFC107', '#009688', '#E91E63']
explode = (0.1, 0, 0)
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Percentage of Prices by Price Range')
plt.show()


# In[9]:


#slide 10
import matplotlib.pyplot as plt
subtotal_data = [35.00, 16.99, 9.99, 147.98, 14.99, 11.99, 38.98, 44.99, 27.30, 37.08, 12.99, 7.20, 27.99, 15.32, 9.95, 38.89, 8.95, 12.99, 7.99, 16.98, 35.00, 7.50, 7.67, 9.80, 13.95, 9.99, 10.98, 32.98, 28.99, 13.88, 11.62, 11.98, 51.99, 10.59, 7.94, 8.32, 25.62, 0.52, 5.43, 12.99, 102.47, 79.97, 49.99, 199.99, 41.97, 15.60, 36.49, 15.95, 99.63, 12.78, 12.78, 6.49, 5.76, 42.93, 49.99, 6.30, 5.99, 35.99, 54.88]
total_charged_data = [36.93, 16.99, 9.99, 156.12, 14.99, 12.65, 40.63, 44.99, 28.80, 37.08, 12.99, 7.60, 27.99, 16.16, 10.50, 38.89, 9.44, 12.99, 7.99, 17.91, 36.92, 7.91, 7.67, 9.80, 13.95, 9.99, 11.58, 33.80, 28.99, 13.88, 12.26, 12.64, 51.99, 10.59, 11.93, 16.28, 26.47, 5.47, 9.42, 12.99, 107.42, 69.97, 45.99, 210.99, 41.97, 16.46, 38.50, 15.95, 102.97, 13.48, 13.48, 6.85, 5.76, 45.29, 34.99, 6.30, 1.04, 35.99, 58.17]
differences = [total_charged_data[i] - subtotal_data[i] for i in range(len(subtotal_data))]
bins = [i * 0.5 for i in range(0, 15)]
plt.hist(differences, bins=bins)
plt.xlabel('Difference in Prices')
plt.ylabel('Frequency')
plt.title('Difference in Prices between Subtotal and Total Charged')
plt.show()


# In[10]:


#slide 11
import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame({
    'Subtotal': [35.00, 16.99, 9.99, 147.98, 14.99, 11.99, 38.98, 44.99, 27.30, 37.08, 12.99, 7.20, 27.99, 15.32, 9.95, 38.89, 8.95, 12.99, 7.99, 16.98, 35.00, 7.50, 7.67, 9.80, 13.95, 9.99, 10.98, 32.98, 28.99, 13.88, 11.62, 11.98, 51.99, 10.59, 7.94, 8.32, 25.62, 0.52, 5.43, 12.99, 102.47, 79.97, 49.99, 199.99, 41.97, 15.60, 36.49, 15.95, 99.63, 12.78, 12.78, 6.49, 5.76, 42.93, 49.99, 6.30, 5.99, 35.99, 54.88],
    'Total Charged': [36.93, 16.99, 9.99, 156.12, 14.99, 12.65, 40.63, 44.99, 28.80, 37.08, 12.99, 7.60, 27.99, 16.16, 10.50, 38.89, 9.44, 12.99, 7.99, 17.91, 36.92, 7.91, 7.67, 9.80, 13.95, 9.99, 11.58, 33.80, 28.99, 13.88, 12.26, 12.64, 51.99, 10.59, 11.93, 16.28, 26.47, 5.47, 9.42, 12.99, 107.42, 69.97, 45.99, 210.99, 41.97, 16.46, 38.50, 15.95, 102.97, 13.48, 13.48, 6.85, 5.76, 45.29, 34.99, 6.30, 1.04, 35.99, 58.17]
})
plt.plot(data['Subtotal'], label='Subtotal')
plt.plot(data['Total Charged'], label='Total Charged')
plt.xlabel('Order')
plt.ylabel('Price')
plt.legend()
plt.show()


# In[13]:


#slide 12
import pandas as pd
subtotal_values = [35.00, 16.99, 9.99, 147.98, 14.99, 11.99, 38.98, 44.99, 27.30, 37.08, 12.99, 7.20, 27.99, 15.32, 9.95, 38.89, 8.95, 12.99, 7.99, 16.98, 35.00, 7.50, 7.67, 9.80, 13.95, 9.99, 10.98, 32.98, 28.99, 13.88, 11.62, 11.98, 51.99, 10.59, 7.94, 8.32, 25.62, 0.52, 5.43, 12.99, 102.47, 79.97, 49.99, 199.99, 41.97, 15.60, 36.49, 15.95, 99.63, 12.78, 12.78, 6.49, 5.76, 42.93, 49.99, 6.30, 5.99, 35.99, 54.88]
subtotal_stats = pd.DataFrame({
    'Average': [sum(subtotal_values)/len(subtotal_values)],
    'Median': [pd.Series(subtotal_values).median()],
    'Max': [max(subtotal_values)],
    'Min': [min(subtotal_values)],
    'Standard Dev': [pd.Series(subtotal_values).std()]
}, index=['Subtotal'])
subtotal_stats


# In[14]:


#continued
import pandas as pd
shipping_charge_values = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 3.99, 7.96, 0.00, 4.95, 3.99, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
shipping_charge_stats = pd.DataFrame({
    'Average': [sum(shipping_charge_values)/len(shipping_charge_values)],
    'Median': [pd.Series(shipping_charge_values).median()],
    'Max': [max(shipping_charge_values)],
    'Min': [min(shipping_charge_values)],
    'Standard Dev': [pd.Series(shipping_charge_values).std()]
}, index=['Shipping Charge'])
shipping_charge_stats


# In[15]:


import pandas as pd
tax_before_promotion_values = [0.00, 0.00, 0.00, 8.14, 0.00, 0.66, 1.65, 0.00, 1.50, 0.00, 0.00, 0.40, 0.00, 0.84, 0.55, 0.00, 0.49, 0.00, 0.00, 0.93, 1.92, 0.41, 0.00, 0.00, 0.00, 0.00, 0.60, 0.82, 0.00, 0.00, 0.64, 0.66, 0.00, 0.00, 0.00, 0.00, 0.85, 0.00, 0.00, 0.00, 4.95, 0.00, 0.00, 11.00, 0.00, 0.86, 2.01, 0.00, 3.34, 0.70, 0.70, 0.36, 0.00, 2.36, 0.00, 0.00, 0.05, 0.00, 3.29]
tax_before_promotion_stats = pd.DataFrame({
    'Average': [sum(tax_before_promotion_values)/len(tax_before_promotion_values)],
    'Median': [pd.Series(tax_before_promotion_values).median()],
    'Max': [max(tax_before_promotion_values)],
    'Min': [min(tax_before_promotion_values)],
    'Standard Dev': [pd.Series(tax_before_promotion_values).std()]
}, index=['Tax Before Promotion'])
tax_before_promotion_stats


# In[16]:


import pandas as pd
total_promotions_values = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 10.00, 4.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 15.00, 0.00, 5.00, 0.00, 0.00]
total_promotions_stats = pd.DataFrame({
    'Average': [sum(total_promotions_values)/len(total_promotions_values)],
    'Median': [pd.Series(total_promotions_values).median()],
    'Max': [max(total_promotions_values)],
    'Min': [min(total_promotions_values)],
    'Standard Dev': [pd.Series(total_promotions_values).std()]
}, index=['Total Promotions'])
total_promotions_stats


# In[17]:


import pandas as pd
tax_values = [1.93, 0.00, 0.00, 8.14, 0.00, 0.66, 1.65, 0.00, 1.50, 0.00, 0.00, 0.40, 0.00, 0.84, 0.55, 0.00, 0.49, 0.00, 0.00, 0.93, 1.92, 0.41, 0.00, 0.00, 0.00, 0.00, 0.60, 0.82, 0.00, 0.00, 0.64, 0.66, 0.00, 0.00, 0.00, 0.00, 0.85, 0.00, 0.00, 0.00, 4.95, 0.00, 0.00, 11.00, 0.00, 0.86, 2.01, 0.00, 3.34, 0.70, 0.70, 0.36, 0.00, 2.36, 0.00, 0.00, 0.05, 0.00, 3.29]
tax_stats = pd.DataFrame({
    'average': [sum(tax_values)/len(tax_values)],
    'Median': [pd.Series(tax_values).median()],
    'Max': [max(tax_values)],
    'Min': [min(tax_values)],
    'Standard Dev': [pd.Series(tax_values).std()]
}, index=['Tax Charged'])
tax_stats = tax_stats.rename(columns={'average': 'Average'})
tax_stats


# In[18]:


import pandas as pd
total_charged_values = [36.93, 16.99, 9.99, 156.12, 14.99, 12.65, 40.63, 44.99, 28.80, 37.08, 12.99, 7.60, 27.99, 16.16, 10.50, 38.89, 9.44, 12.99, 7.99, 17.91, 36.92, 7.91, 7.67, 9.80, 13.95, 9.99, 11.58, 33.80, 28.99, 13.88, 12.26, 12.64, 51.99, 10.59, 11.93, 16.28, 26.47, 5.47, 9.42, 12.99, 107.42, 69.97, 45.99, 210.99, 41.97, 16.46, 38.50, 15.95, 102.97, 13.48, 13.48, 6.85, 5.76, 45.29, 34.99, 6.30, 1.04, 35.99, 58.17]
total_charged_stats = pd.DataFrame({
    'Average': [sum(total_charged_values)/len(total_charged_values)],
    'Median': [pd.Series(total_charged_values).median()],
    'Max': [max(total_charged_values)],
    'Min': [min(total_charged_values)],
    'Standard Dev': [pd.Series(total_charged_values).std()]
}, index=['Total Charged'])
total_charged_stats


# In[ ]:




