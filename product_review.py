import openai
import pandas as pd
import time

#Collect your OpenAI API Key
openai.api_key = "Your OpenAI API KEY"
df = pd.read_csv('vitamines_pillen.csv')


for x in range(0, len(df)):
        #Opening the required parameter from csv file
        prduct_name = df['Name'][x]
        product_des_1 = df['Short Description 1'][x]
        product_des_2 = df['Short Description 2'][x]
        
        #Creating the prompt
        product = f"You talk in the Dutch language. Now, you have to write a product review for a product. The information about the product is given below.\n\nProduct Name: {prduct_name}\n\nProduct Description: {product_des_1}\n{product_des_2}\n\nThink that you have bought this product. Now write two realistic, unique, and positive product reviews for this product."

        time.sleep(10)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": product}]
        )
        time.sleep(1)

        review = completion.choices[0].message.content
        df.iloc[x, 6] = review
        print(f"{x} Review Stored in Csv file.")

df.to_csv("vitamines_pillen.csv")

print("Review creating is completed")