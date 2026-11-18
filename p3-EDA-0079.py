import pandas as pd
import matplotlib.pyplot as plt
parcelas_cultivo = {
    'id_parcela': [101, 102, 103, 104, 105, 106],
    'nombre_parcela': ['El Mirador', 'La Esperanza', 'San Jose', 'El Roble', 'La Pradera', 'Los Pinos'],
    'hectareas': [5.5, 3.2, 8.0, 2.5, 10.0, 4.0],
    'tipo_cultivo': ['Maiz', 'Trigo', 'Maiz', 'Frijol', 'Soya', 'Trigo'],
    'fecha_siembra': ['2023-05-01', '2023-10-15', '2023-05-10', '2023-06-01', '2023-06-15', '2023-10-20'],
    'fecha_cosecha_estimada': ['2023-09-01', '2024-03-15', '2023-09-10', '2023-10-01', '2023-11-15', '2024-03-20'],
    'riego': ['Aspersión', 'Goteo', 'Aspersión', 'Temporal', 'Goteo', 'Goteo'],
    'rendimiento_estimado_ton': [22.0, 12.8, 32.0, 5.0, 30.0, 16.0],
    'trabajador_responsable': ['Juan', 'Pedro', 'Juan', 'Luis', 'Carlos', 'Pedro'],
    'estado': ['Cosechado', 'En crecimiento', 'Cosechado', 'Cosechado', 'Cosechado', 'En crecimiento']
}
print("Análisis exploratorio de datos (EDA, Exploratory Data Analysis) por Iram Jimenez NC = 0079")
print("5. Crear el diccionario con 10 listas y 6 elementos")
# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(parcelas_cultivo)
print("\n--- TABLA ORIGINAL DE CULTIVOS ---")
print(df)
# 3. Exportar los datos a CSV
df.to_csv(
    'parcelas_cultivo.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("Datos leidos desde el archivo csv")
print("parcelas_cultivo.csv")
print("8. Leer los datos desde el archivo csv")
# 4. Leer el archivo CSV
df = pd.read_csv('parcelas_cultivo.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print("9. Análisis Exploratorio de Datos (EDA)")
# 5. Primeros y últimos registros
print("\n1. PRIMEROS REGISTROS (Head):")
print(df.head(3)) # Muestra los primeros 3
print("\n2. ÚLTIMOS REGISTROS (Tail):")
print(df.tail(2)) # Muestra los últimos 2
print("6. Dimensiones y estructura")
print(df)
# 6. Dimensiones y estructura
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("7. Estadísticas y limpieza")
# 7. Estadísticas y limpieza
print("\n7. ESTADÍSTICAS DESCRIPTIVAS:")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Hectareas únicas:", df['hectareas'].unique())

print("8 y 9. Ordenamiento, filtrado y agrupación")
print(df)
# 8. Análisis específico
print("\n11. Numero de hectareas:")
print(df['hectareas'].value_counts())

print("\n12. PROMEDIO DE RENDIMIENTO: $", df['rendimiento_estimado_ton'].mean())
print("13. RENDIMIENTO MÁXIMO: $", df['rendimiento_estimado_ton'].max())
print("14. RENDIMIENTO MÍNIMO: $", df['rendimiento_estimado_ton'].min())

# 9. Ordenamiento, filtrado y agrupación
print("\n15. RENDIMIENTO ESTIMADO POR TONELADA (Mayor a menor):")
print(df.sort_values(by='rendimiento_estimado_ton', ascending=False))

print("\n16. RENDIMIENTO ESTIMADO MAYOR A 15:")
filtro = df[df['rendimiento_estimado_ton'] > 15]
print(filtro)

print("\n17. RESUMEN POR PARCELAS:")
resumen = df.groupby('hectareas').agg(
    parcelas=('id_parcela', 'count'),
    rendimiento_promedio=('rendimiento_estimado_ton', 'mean'),
    tonelada_maxima=('rendimiento_estimado_ton', 'max')
)
print(resumen)

# 18. Gráfica de barras: Parcelas por tipo de cultivo
conteo = df['tipo_cultivo'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Parcelas por tipo de cultivo')
plt.xlabel('Tipo de cultivo')
plt.ylabel('Cantidad de parcelas')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Rendimiento estimado por parcela
plt.figure(figsize=(8, 5))
plt.bar(df['nombre_parcela'], df['rendimiento_estimado_ton'], color='lightgreen')
plt.title('Rendimiento estimado por parcela')
plt.xlabel('Parcela')
plt.ylabel('Rendimiento (toneladas)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de hectáreas
plt.figure(figsize=(8, 5))
plt.hist(df['hectareas'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de hectáreas de las parcelas')
plt.xlabel('Hectáreas')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Hectáreas vs Rendimiento estimado
plt.figure(figsize=(8, 5))
plt.scatter(df['hectareas'], df['rendimiento_estimado_ton'], color='red', s=100)
plt.title('Relación entre hectáreas y rendimiento estimado')
plt.xlabel('Hectáreas')
plt.ylabel('Rendimiento estimado (toneladas)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de rendimiento estimado
plt.figure(figsize=(7, 5))
plt.boxplot(df['rendimiento_estimado_ton'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de rendimiento estimado (Boxplot)')
plt.ylabel('Rendimiento (toneladas)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas')
plt.tight_layout()
plt.show()