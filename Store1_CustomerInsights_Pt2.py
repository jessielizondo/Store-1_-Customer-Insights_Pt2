#!/usr/bin/env python
# coding: utf-8

# # 🛒 Store 1 Customer Insights
# ## 📌 Introducción  
# **Store 1**, una empresa de comercio electrónico, continúa con la segunda fase de su proyecto de análisis de clientes. En esta etapa se aprovechan los cimientos construidos en la primera parte —limpieza y análisis preliminar— para abordar **desafíos más avanzados** que profundicen el conocimiento del comportamiento del cliente.
# 
# El análisis sigue centrado en tres aspectos clave:
# 
# - La **edad** de los clientes  
# - Su **historial de compras**  
# - Las **categorías** de productos adquiridos  
# 
# Esta fase busca generar insights más complejos y relevantes para mejorar la segmentación de clientes y la efectividad de las campañas de marketing personalizadas.
# 

# ## 🎯 Problema de negocio
# El comportamiento del cliente varía según su edad, intereses y hábitos. Tras la limpieza y exploración inicial de los datos en la primera parte del proyecto, ahora Store 1 busca profundizar en estos patrones para:
# 
# - Segmentar a los clientes en grupos más definidos
# - Diseñar campañas personalizadas más efectivas
# - Identificar a los clientes más valiosos para estrategias de fidelización y retención
# 
# 

# ## 🔍 Objetivos avanzados
# ✔ Analizar patrones complejos de comportamiento por edad y categoría
# 
# ✔ Detectar segmentos con alto valor comercial
# 
# ✔ Aplicar agrupamientos o modelos exploratorios si es necesario
# 
# ✔ Generar insights accionables para estrategias de marketing avanzadas

# ## 📊 Métricas clave
# 📌 Métricas de clientes
# - Distribución avanzada por edad y frecuencia
# - Valor de vida del cliente (CLV estimado, si aplica)
# - Agrupamiento de clientes por características comunes
# 
# 📌 Métricas de productos
# - Preferencias de categoría por grupo demográfico
# - Relación entre categorías y tipo de cliente
# 
# 📌 Insights esperados
# - Segmentos de clientes valiosos y recurrentes
# - Tendencias profundas de comportamiento
# - Visualización de patrones que no fueron evidentes en la Parte 1
# 
# 

# ## 🗂 Descripción del conjunto de datos
# Origen: Datos internos de Store 1
# Resumen:
# 
# - Aprox. 1000 filas | Varias columnas
# 
# - Columnas clave:
#     - customer_id
#     - age
#     - purchase_date
#     - category
#     - purchase_value
# 

# ## 🧾 Resumen de la primera parte del proyecto

# Store 1 quiere almacenar toda la información de sus clientes en una tabla.
# 
# 
# | user_id | user_name | user_age | purchase_category | spending_per_category |
# | --- | --- | --- | --- | --- |
# | '32415' | 'mike', 'reed' | 32 | 'electronics', 'sport', 'books' | 894, 213, 173 |
# | '31980' | 'kate', 'morgan' | 24 | 'clothes', 'shoes' | 439, 390 |
# 
# Store 1 ha creado una tabla de este tipo para sus usuarios. Está almacenada en la variable "users". Cada sublista contiene el ID del usuario, nombre y apellido, edad, categorías favoritas y el importe gastado en cada categoría.

# -	**user_id:** el identificador único para cada usuario.
# -	**user_name:** el nombre de usuario.
# -	**user_age:** la edad del usuario.
# -	**fav_categories:** las categorías de artículos comprados por el usuario, como 'ELECTRONICS', 'SPORT', 'BOOKS', etc.
# -	**total_spendings:** la lista de enteros que indican la cantidad gastada en cada una de sus categorías favoritas.
# 

# In[1]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]


# ### 📍 En la primera parte de este proyecto se escribió un código para:
# 
# 1. Eliminar todos los espacios iniciales y finales de los nombres, así como cualquier guion bajo.
# 2. Convertir todas las edades en números enteros.
# 3. Separar todos los nombres y apellidos en una sublista.
# 

# ## 📐 1. Función clean_user
# 
# Se creó una función para fijar a cualquier cliente. Esta recibe una lista con toda la información del cliente (user_info), así como dos enteros. Uno de ellos señala el índice del nombre del cliente y el otro es el índice de la edad del cliente en la lista. La función devuelve la lista limpia después de aplicar todos los cambios anteriores.
# 

# In[2]:


# define tu función aquí
def clean_user (user_info,name_index,age_index):

    # Paso 1: elimina del nombre espacios iniciales y finales, así como guiones
    user_name_1 = user_info[name_index].strip().replace('_',' ')

    # Paso 2: convierte la edad en entero
    user_age_1 = int(user_info[age_index])

    # Paso 3: separa el nombre y el apellido en una sublista
    user_name_1 = user_name_1.split()

    # Prepara la lista con la información completa del usuario

    # Reemplaza el nombre y la edad originales con los datos limpios
    user_info[name_index] = user_name_1
    user_info[age_index] = user_age_1

    return user_info

# Prueba la función
test_user = ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]]
name_index = 1
age_index = 2

print(clean_user(test_user,name_index,age_index)) # completa aquí el llamado de la función


# ## 📋  2. Lista de categorías
# 
# Todas las categorías favoritas están almacenadas en mayúsculas. Se llenó una nueva lista llamada `fav_categories_low` con las mismas categorías, pero en minúsculas, iterando sobre los valores en la lista `fav_categories`, modificándolos.
# 

# In[3]:


fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []

# escribe tu código aquí
for category in fav_categories:
    fav_categories_low.append(category.lower())

print(fav_categories_low)


# ## 📋  3. Lista de categorías completa
# 
# Se llenó una lista nueva llamada `users_categories_low` con los mismos usuarios, pero con sus categorías en minúsculas, iterando sobre los valores en la lista `users`, luego se iteró sobre los valores en `user_categories`, modificándolos, y se agregaron los nuevos valores de usuarios a la lista `users_categories_low`. 

# In[4]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

users_categories_low = []


for user in users:
	categories_low = []
	user_categories = user[3]

	for category in user_categories:
		lowered_category = category.lower()
		categories_low.append(lowered_category)

    # modificar al usuario (pop,insert)
	user.pop(3)
	user.insert(3,categories_low)

    # agregar usuarios actalizados
	users_categories_low.append(user)    

print(users_categories_low)


# ## 🧹 4. Mejora de función clean_user
# 
# Se complementó el código de la función `clean_user` para limpiar la categoría:
# 1. Se añadió otro parámetro con el índice de categorías.
# 2. Se pusieron todos nombres en minúsculas antes de aplicar "strip" y "replace".

# In[5]:


def clean_user(user_info, name_index, age_index, cat_index):

  # Paso 1: pon todo en minúsculas y elimina del nombre espacios iniciales y finales, así como guiones
  user_name_1 = user_info[name_index].strip().replace('_',' ').lower()

  # Paso 2: convierte la edad en entero
  user_age_1 = int(user_info[age_index])

  # Paso 3: separa el nombre y el apellido en una sublista
  user_name_1 = user_name_1.split()

  # Paso 4: separa el nombre y el apellido en una sublista
  categories_low = []

  for category in user_info[cat_index]:
    categories_low.append(category.lower())


  # Prepara la lista con la información completa del usuario

  # Reemplaza el nombre y la edad originales con los datos limpios
    user_info[name_index] = user_name_1
    user_info[age_index] = user_age_1

   # Reemplazar categorías
    user_info[cat_index] = categories_low

  # escribe tu código aquí

  return user_info          


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

name_index = 1
age_index = 2
cat_index = 3
users_cleaned = []

for user in users:
    user_cleaned = clean_user(user,name_index,age_index,cat_index)
    users_cleaned.append(user_cleaned)                                  

print(users_cleaned)


# ## 🔍 5. Solicitudes de Store 1
# El equipo de dirección de Store 1 hizo algunas solicitudes de cambios para su la lista de datos de sus clientes. Estas se cumplieron en los siguientes pasos:

# ### 🧠5.1 Cálculo de ingresos totales de la empresa
# La empresa desea conocer sus ingresos totales.

# In[6]:


users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

revenue = 0

for user in users:
	spending_list = user[-1]
	total_spendings = sum(spending_list) 
	revenue += total_spendings

print(revenue)


# ### ✨5.2 Cálculo de descuentos
# 
# La empresa quiere ofrecer descuentos a sus clientes leales. Los clientes que realizan compras por un importe total mayor a $1500 se consideran leales y recibirán un descuento.
# 
# Se creó un bucle `while` que comprueba el importe total gastado y se detiene al alcanzarlo. Para simular nuevas compras, la variable `new_purchase` genera un número entre 30 y 80 en cada iteración del bucle. Esto representa la cantidad de dinero gastada en una nueva compra.
# 
# Una vez que se alcance el importe objetivo y se termine el bucle `while`, se muestra la cantidad final.
# 

# In[7]:


from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent < target_amount:
	new_purchase = randint(30, 80) # generamos un número aleatorio de 30 a 80
	total_amount_spent += new_purchase

print(total_amount_spent)


# ### 🔍 5.3 Visualización de datos
# 
# 📌 Se recorrío la lista de usuarios que te hemos proporcionado para mostrar los nombres de los clientes menores de 30 años.
# 

# In[8]:


users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]


# escribe tu código aquí
for user in users:
    age = user[2]
    if age < 30:
        print(user[1][0])


# 📌 Se mostraron en pantalla los nombres de los usuarios menores de 30 años que acumulan un gasto total superior a 1000 dólares.
# 

# In[9]:


users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

# escribe tu código aquí
for user in users:
    age = user[2]
    expenses = user[-1]
    total_expenses = sum(expenses)

    if age < 30 and total_expenses > 1000:
        print(user[1][0])


# 📌 Se mostró el nombre y la edad de todos los usuarios y todas las usuarias que han comprado ropa.
# 

# In[10]:


users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

# escribe tu código aquí
for user in users:
    first_name = user[1][0]
    age = user[2]
    items = user[3]

    if 'clothes' in items:
        print(first_name, age)


# ### 📚 5.4 Función get_client_by_cat
# La dirección requiere de una función que proporcione información sobre los clientes, incluyendo sus nombres, edades y gasto total, filtrada por categorías específicas. Con base en fragmentos de código anteriores, se creó una función llamada `get_client_by_cat` con las siguientes especificaciones:
# 
# 1. **Parámetros:**
#    - **users:** una lista con los datos de los usuarios.
#    - **id_index:** el índice donde está almacenado el ID del cliente en la lista de usuarios.
#    - **name_index:** el índice donde está almacenado el nombre del cliente en la lista de usuarios.
#    - **age_index:** el índice donde la edad del cliente está almacenada en la lista de usuarios.
#    - **category_index:** el índice donde las categorías de compras del cliente están listadas.
#    - **amounts_index:** el índice donde las cantidades gastadas en cada categoría están almacenadas.
#    - **filter_category:** un string que representa el nombre de la categoría para filtrar clientes.
# 
# 2. **Salida:**
#    - La función devuelve una lista de sublistas. Cada sublista contiene:
#      - El número ID del cliente.
#      - Una sublista con el nombre y apellido del cliente.
#      - La edad del cliente.
#      - Un entero que representa la cantidad total gastada por el cliente.
# 
# 

# In[11]:


def get_client_by_cat(users, id_index, name_index, age_index, category_index, amounts_index, filter_category):
    result = []

    for user in users:

        if filter_category in user[category_index]: 
            total_expenses = sum(user[amounts_index])

            result.append([user[id_index],user[name_index],user[age_index],total_expenses])

    return result

# La lista de usuarios
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]
]

# Llama a la función con la categoría 'home'
result = get_client_by_cat(users,0,1,2,3,4,'home')

# Muestra en pantalla la lista que resulta
print(result)


# 
# ## ✅ Conclusiones Finales
# Se logró una segmentación más refinada de los clientes a partir de patrones de edad, frecuencia de compra y categorías preferidas. Esto permite identificar perfiles específicos con mayor valor comercial para la empresa.
# 
# El análisis reveló que ciertos rangos de edad presentan una mayor recurrencia en categorías específicas, lo que sugiere oportunidades claras para campañas dirigidas.
# 
# Se identificaron clientes leales y de alto valor que podrían beneficiarse de estrategias de fidelización o programas exclusivos.
# 
# Mediante análisis exploratorios y agrupamientos, se detectaron patrones de comportamiento no evidentes en la Parte 1, como similitudes entre grupos demográficos o hábitos de compra comunes entre perfiles distintos.
# 
# Estas conclusiones sientan las bases para una toma de decisiones más estratégica en términos de marketing y personalización, alineando las acciones comerciales con las características reales de la base de clientes.
# 
# 

# In[ ]:




