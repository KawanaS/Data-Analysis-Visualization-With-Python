import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

desired_width=400
pd.set_option('display.width',desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

prod_info=pd.read_csv('scraped_info.csv',names=['Product_title','Price','Seller','Rated','Link'])
spec_chars=['Rating','+',',']
for char in spec_chars:
    prod_info['Rated']=prod_info['Rated'].str.replace(char,' ')
    prod_info['Price'] = prod_info['Price'].str.replace(char, '')

#drop NANs
prod_info=prod_info[prod_info['Seller'].notna()]
prod_info=prod_info[prod_info['Rated'].notna()]

#print the datatype
#print(prod_info.Rated.dtype)

#Convert datatypes to numeric
prod_info['Price']=pd.to_numeric(prod_info['Price'])
prod_info['Rated']=pd.to_numeric(prod_info['Rated'])

#visualize the rates of each product
'''product_rates=prod_info.groupby('Product_title').sum()['Rated']
products=[product for product,df in prod_info.groupby('Product_title')]
prices=prod_info.groupby('Product_title').mean()['Price']
plt.subplot(1, 2, 1)
fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.bar(products,product_rates)
ax2.plot(products,prices,'b-')
ax1.set_xticklabels(products,rotation='vertical',size=4)
ax1.set_xlabel('Products')
ax1.set_ylabel('Ratings')
ax2.set_ylabel('Price')'''

#visualize the ratings of each seller
seller_rates=prod_info.groupby('Seller').mean()['Rated']
sellers=[seller for seller,df in prod_info.groupby('Seller')]
plt.bar(sellers,seller_rates)
plt.xlabel('Sellers')
plt.ylabel('Ratings')
plt.show()

print(prod_info)
#prod_info.to_excel('scraped_info125.xlsx',index=False)
