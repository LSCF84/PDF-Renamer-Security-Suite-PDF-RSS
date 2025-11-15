import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import pandas as pd
import os
from pathlib import Path

class GeneradorExcelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Excel para PDFs - Asistente Completo")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Variables
        self.tipo_seleccionado = tk.StringVar(value="general")
        self.archivo_excel = tk.StringVar()
        self.directorio_pdfs = tk.StringVar()
        self.directorio_salida = tk.StringVar(value="./Documentos_Procesados")
        
        self.estructuras = {
            "general": {
                "nombre": "General",
                "columnas": ["ID_Archivo", "Nombre_Salida", "Password"],
                "ejemplo": [
                    ["DOC001", "Informe_Final_Proyecto", "clave123"],
                    ["DOC002", "Presentacion_Reunion", "clave456"],
                    ["DOC003", "Manual_Usuario", "clave789"]
                ]
            },
            "facturas": {
                "nombre": "Facturas",
                "columnas": ["Numero_Factura", "Cliente_Fecha", "Clave_Acceso"],
                "ejemplo": [
                    ["FAC-001", "ClienteA_Enero_2024", "fact123"],
                    ["FAC-002", "ClienteB_Enero_2024", "fact456"],
                    ["FAC-003", "ClienteC_Febrero_2024", "fact789"]
                ]
            },
            "contratos": {
                "nombre": "Contratos",
                "columnas": ["Referencia", "Nombre_Contrato", "Password"],
                "ejemplo": [
                    ["CONT-2024-001", "EmpresaX_Contrato_Servicios", "contra123"],
                    ["CONT-2024-002", "EmpresaY_Acuerdo_Confidencial", "contra456"]
                ]
            },
            "pacientes": {
                "nombre": "Pacientes",
                "columnas": ["Nº de paciente", "Nombre", "DNI"],
                "ejemplo": [
                    ["001", "Juan Pérez García", "12345678A"],
                    ["002", "María López Martínez", "87654321B"],
                    ["003", "Carlos Rodríguez Silva", "11223344C"]
                ]
            },
            "educativo": {
                "nombre": "Recursos Educativos",
                "columnas": ["Codigo_Recurso", "Tema_Nombre", "Clave"],
                "ejemplo": [
                    ["MAT-001", "Algebra_Basica", "mate123"],
                    ["MAT-002", "Geometria_Avanzada", "mate456"],
                    ["FIS-001", "Mecanica_Clasica", "fisica123"]
                ]
            },
            "legal": {
                "nombre": "Documentos Legales",
                "columnas": ["Expediente", "Documento_Nombre", "Password"],
                "ejemplo": [
                    ["EXP-2024-01", "Demanda_Civil", "legal123"],
                    ["EXP-2024-02", "Contrato_Arrendamiento", "legal456"]
                ]
            }
        }
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Notebook (pestañas)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Pestaña 1: Selección de estructura
        self.frame_seleccion = ttk.Frame(notebook)
        notebook.add(self.frame_seleccion, text="1. Seleccionar Estructura")
        
        # Pestaña 2: Edición de datos
        self.frame_edicion = ttk.Frame(notebook)
        notebook.add(self.frame_edicion, text="2. Editar Datos")
        
        # Pestaña 3: Procesar PDFs
        self.frame_procesar = ttk.Frame(notebook)
        notebook.add(self.frame_procesar, text="3. Procesar PDFs")
        
        self.crear_pestana_seleccion()
        self.crear_pestana_edicion()
        self.crear_pestana_procesar()
    
    def crear_pestana_seleccion(self):
        # Título
        titulo = ttk.Label(self.frame_seleccion, 
                          text="Selecciona el tipo de documentos a procesar",
                          font=('Arial', 14, 'bold'))
        titulo.pack(pady=20)
        
        # Frame para los botones de estructura
        frame_estructuras = ttk.Frame(self.frame_seleccion)
        frame_estructuras.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Crear botones para cada estructura
        row, col = 0, 0
        for key, estructura in self.estructuras.items():
            btn = ttk.Radiobutton(
                frame_estructuras,
                text=estructura["nombre"],
                variable=self.tipo_seleccionado,
                value=key,
                command=self.mostrar_vista_previa
            )
            btn.grid(row=row, column=col, sticky='w', padx=10, pady=5)
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        # Vista previa
        ttk.Label(self.frame_seleccion, text="Vista previa de la estructura:", 
                 font=('Arial', 10, 'bold')).pack(pady=(20, 5))
        
        self.texto_vista_previa = scrolledtext.ScrolledText(
            self.frame_seleccion, 
            height=8, 
            width=80,
            font=('Consolas', 9)
        )
        self.texto_vista_previa.pack(pady=5, padx=20, fill='both', expand=True)
        
        # Botón generar Excel
        btn_generar = ttk.Button(
            self.frame_seleccion,
            text="Generar Archivo Excel",
            command=self.generar_excel
        )
        btn_generar.pack(pady=20)
        
        # Mostrar vista previa inicial
        self.mostrar_vista_previa()
    
    def crear_pestana_edicion(self):
        # Instrucciones
        instrucciones = ttk.Label(self.frame_edicion,
                                text="Carga el Excel generado y edita los datos directamente en la tabla",
                                font=('Arial', 11))
        instrucciones.pack(pady=10)
        
        # Frame para controles
        frame_controles = ttk.Frame(self.frame_edicion)
        frame_controles.pack(pady=10, fill='x')
        
        ttk.Button(frame_controles, 
                  text="Cargar Excel", 
                  command=self.cargar_excel).pack(side='left', padx=5)
        
        ttk.Button(frame_controles, 
                  text="Guardar Cambios", 
                  command=self.guardar_cambios).pack(side='left', padx=5)
        
        ttk.Button(frame_controles, 
                  text="Añadir Fila", 
                  command=self.anadir_fila).pack(side='left', padx=5)
        
        ttk.Button(frame_controles, 
                  text="Eliminar Fila Seleccionada", 
                  command=self.eliminar_fila).pack(side='left', padx=5)
        
        # Treeview para edición
        self.crear_tabla_edicion()
    
    def crear_tabla_edicion(self):
        # Frame para la tabla con scroll
        frame_tabla = ttk.Frame(self.frame_edicion)
        frame_tabla.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Scrollbars
        vscroll = ttk.Scrollbar(frame_tabla, orient='vertical')
        hscroll = ttk.Scrollbar(frame_tabla, orient='horizontal')
        
        # Treeview
        self.tabla = ttk.Treeview(frame_tabla, 
                                 yscrollcommand=vscroll.set,
                                 xscrollcommand=hscroll.set)
        
        vscroll.config(command=self.tabla.yview)
        hscroll.config(command=self.tabla.xview)
        
        # Empaquetar
        self.tabla.pack(side='left', fill='both', expand=True)
        vscroll.pack(side='right', fill='y')
        hscroll.pack(side='bottom', fill='x')
    
    def crear_pestana_procesar(self):
        # Configuración de procesamiento
        frame_config = ttk.LabelFrame(self.frame_procesar, text="Configuración de Procesamiento")
        frame_config.pack(pady=10, padx=20, fill='x')
        
        # Directorio de PDFs originales
        ttk.Label(frame_config, text="Directorio con PDFs originales:").grid(row=0, column=0, sticky='w', pady=5)
        ttk.Entry(frame_config, textvariable=self.directorio_pdfs, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame_config, text="Examinar", command=self.examinar_directorio_pdfs).grid(row=0, column=2, padx=5)
        
        # Directorio de salida
        ttk.Label(frame_config, text="Directorio de salida:").grid(row=1, column=0, sticky='w', pady=5)
        ttk.Entry(frame_config, textvariable=self.directorio_salida, width=50).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(frame_config, text="Examinar", command=self.examinar_directorio_salida).grid(row=1, column=2, padx=5)
        
        # Archivo Excel
        ttk.Label(frame_config, text="Archivo Excel:").grid(row=2, column=0, sticky='w', pady=5)
        ttk.Entry(frame_config, textvariable=self.archivo_excel, width=50).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(frame_config, text="Examinar", command=self.examinar_archivo_excel).grid(row=2, column=2, padx=5)
        
        # Opciones de procesamiento
        frame_opciones = ttk.LabelFrame(self.frame_procesar, text="Opciones")
        frame_opciones.pack(pady=10, padx=20, fill='x')
        
        self.proteger_pdf = tk.BooleanVar(value=True)
        ttk.Checkbutton(frame_opciones, text="Proteger PDFs con contraseña", 
                       variable=self.proteger_pdf).pack(anchor='w', pady=5)
        
        self.renombrar_solo = tk.BooleanVar(value=False)
        ttk.Checkbutton(frame_opciones, text="Solo renombrar (sin protección)", 
                       variable=self.renombrar_solo).pack(anchor='w', pady=5)
        
        # Botón procesar
        ttk.Button(self.frame_procesar, 
                  text="PROCESAR PDFs", 
                  command=self.procesar_pdfs,
                  style='Accent.TButton').pack(pady=20)
        
        # Área de log
        ttk.Label(self.frame_procesar, text="Log de ejecución:").pack(anchor='w', padx=20)
        self.texto_log = scrolledtext.ScrolledText(self.frame_procesar, height=15)
        self.texto_log.pack(pady=10, padx=20, fill='both', expand=True)
    
    def mostrar_vista_previa(self):
        estructura = self.estructuras[self.tipo_seleccionado.get()]
        
        # Crear texto de vista previa
        texto = f"Estructura: {estructura['nombre']}\n\n"
        texto += "Columnas:\n"
        texto += " | ".join(estructura['columnas']) + "\n\n"
        texto += "Ejemplo de datos:\n"
        
        for fila in estructura['ejemplo']:
            texto += " | ".join(fila) + "\n"
        
        texto += f"\nTotal de columnas: {len(estructura['columnas'])}"
        
        self.texto_vista_previa.delete('1.0', tk.END)
        self.texto_vista_previa.insert('1.0', texto)
    
    def generar_excel(self):
        try:
            estructura = self.estructuras[self.tipo_seleccionado.get()]
            
            # Pedir ubicación para guardar
            archivo = filedialog.asksaveasfilename(
                title="Guardar Excel como",
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
            )
            
            if archivo:
                # Crear DataFrame con datos de ejemplo
                df = pd.DataFrame(estructura['ejemplo'], columns=estructura['columnas'])
                df.to_excel(archivo, index=False)
                
                self.archivo_excel.set(archivo)
                messagebox.showinfo("Éxito", f"Excel generado correctamente en:\n{archivo}")
                
                # Cargar el Excel recién generado en la pestaña de edición
                self.cargar_excel_en_tabla(archivo)
        
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el Excel:\n{str(e)}")
    
    def cargar_excel(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        
        if archivo:
            self.archivo_excel.set(archivo)
            self.cargar_excel_en_tabla(archivo)
    
    def cargar_excel_en_tabla(self, archivo):
        try:
            df = pd.read_excel(archivo)
            
            # Limpiar tabla existente
            for item in self.tabla.get_children():
                self.tabla.delete(item)
            
            # Configurar columnas
            self.tabla['columns'] = list(df.columns)
            self.tabla['show'] = 'headings'
            
            for col in df.columns:
                self.tabla.heading(col, text=col)
                self.tabla.column(col, width=100)
            
            # Insertar datos
            for _, row in df.iterrows():
                self.tabla.insert('', 'end', values=list(row))
            
            messagebox.showinfo("Éxito", f"Excel cargado: {len(df)} filas")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el Excel:\n{str(e)}")
    
    def guardar_cambios(self):
        if not self.archivo_excel.get():
            messagebox.showwarning("Advertencia", "Primero carga o genera un archivo Excel")
            return
        
        try:
            # Recoger datos de la tabla
            datos = []
            for item in self.tabla.get_children():
                valores = self.tabla.item(item)['values']
                datos.append(valores)
            
            if datos:
                columnas = self.tabla['columns']
                df = pd.DataFrame(datos, columns=columnas)
                df.to_excel(self.archivo_excel.get(), index=False)
                messagebox.showinfo("Éxito", f"Cambios guardados: {len(df)} filas")
            else:
                messagebox.showwarning("Advertencia", "No hay datos para guardar")
        
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los cambios:\n{str(e)}")
    
    def anadir_fila(self):
        if hasattr(self, 'tabla') and self.tabla['columns']:
            # Añadir fila vacía
            valores_vacios = ['' for _ in self.tabla['columns']]
            self.tabla.insert('', 'end', values=valores_vacios)
    
    def eliminar_fila(self):
        seleccion = self.tabla.selection()
        if seleccion:
            for item in seleccion:
                self.tabla.delete(item)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una fila para eliminar")
    
    def examinar_directorio_pdfs(self):
        directorio = filedialog.askdirectory(title="Seleccionar directorio con PDFs originales")
        if directorio:
            self.directorio_pdfs.set(directorio)
    
    def examinar_directorio_salida(self):
        directorio = filedialog.askdirectory(title="Seleccionar directorio de salida")
        if directorio:
            self.directorio_salida.set(directorio)
    
    def examinar_archivo_excel(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if archivo:
            self.archivo_excel.set(archivo)
    
    def log(self, mensaje):
        self.texto_log.insert(tk.END, mensaje + "\n")
        self.texto_log.see(tk.END)
        self.root.update()
    
    def procesar_pdfs(self):
        # Validaciones
        if not self.archivo_excel.get():
            messagebox.showerror("Error", "Selecciona un archivo Excel")
            return
        
        if not self.directorio_pdfs.get():
            messagebox.showerror("Error", "Selecciona el directorio con los PDFs originales")
            return
        
        if not os.path.exists(self.archivo_excel.get()):
            messagebox.showerror("Error", "El archivo Excel no existe")
            return
        
        # Ejecutar procesamiento (aquí integrarías el código original)
        self.log("=== INICIANDO PROCESAMIENTO ===")
        self.log(f"Excel: {self.archivo_excel.get()}")
        self.log(f"PDFs originales: {self.directorio_pdfs.get()}")
        self.log(f"Directorio salida: {self.directorio_salida.get()}")
        
        # Aquí iría la integración con el código de procesamiento PDF
        # Por ahora solo simulamos
        self.log("Procesamiento simulado - Integra aquí el código original")
        self.log("✓ PDFs procesados correctamente")
        self.log("=== PROCESAMIENTO COMPLETADO ===")
        
        messagebox.showinfo("Procesamiento", 
                           "Procesamiento completado.\n\nNota: Para funcionalidad completa, integra el código de procesamiento PDF en este método.")

def main():
    root = tk.Tk()
    app = GeneradorExcelGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()