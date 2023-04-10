text = "('ut ipsam dolores', 57, 257), ('qui veritatis eligendi', 62, 257),  ('eum mollitia odit', 69, 257)" #example_date
new_text = text.replace('),','),\n') 
print(new_text)



#if you want to genarate the output in a txt file use this lines below
with open('tags_1.txt', 'w') as file:
    file.write(new_text)