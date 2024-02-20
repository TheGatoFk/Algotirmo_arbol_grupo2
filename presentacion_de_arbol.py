
"""__init__(): Constructor
agregarHijo(datos): agrega un hijo al nodo actual
obtenerNivel(): devuelve el nivel del nodo actual
buscar(elemento): verifica si el elemento está presente en el árbol
obtenerRaiz(): devuelve el nodo raíz principal del árbol
obtenerPadre(elemento): obtiene el nodo padre de los datos dados (si existe)
obtenerHijos(): devuelve una lista de los hijos del nodo actual
imprimir(): imprime todos los nodos de árbol en orden jerárquico con la cantidad de hijos
imprimir(nivel=1): imprime el árbol hasta el nivel dado con la cantidad de hijos
imprimir(nivel='HR'): imprime el árbol del nombre de nodo dado con la cantidad de hijos

"""
class Arbol:
    def __init__(self, datos): 
        self.datos = datos
        self.hijos = []
        self.padre = None
    
    def agregarHijo(self, datos): 
        datos.padre = self
        self.hijos.append(datos)

    def obtenerNivel(self): 
        i, j = 0, self
        while j.padre: i, j = i+1, j.padre
        return i

    def buscar(self, elemento): 
        if self.datos == elemento:
            return True
        for i in self.hijos: 
            if i.buscar(elemento):
                return True
        return False

    def obtenerPadre(self, elemento): 
        if self.hijos == []:
            return
        
        for i in self.hijos:
            if i.datos == elemento:
                return i.padre.datos
            temp = i.obtenerPadre(elemento)
            if temp:
                return temp

        if elemento == self.obtenerRaiz():
            return "YA ESTÁ EN EL NODO RAÍZ"

    def obtenerHijos(self): 
        return [hijo.datos for hijo in self.hijos]
    
    def obtenerRaiz(self): 
        if not self.padre:
            return self.datos
        return self.padre.obtenerRaiz()

    def imprimir(self, nombre_nivel=None, nivel=None): 
        if not nombre_nivel and not nivel and nivel != 0:
            print(self.obtenerNivel() * "    ", '->', self.datos, f"[{len(self.hijos)} hijos]")
        if self.padre and nombre_nivel == self.padre.datos:
            print(self.obtenerNivel() * "    ", '->', self.datos, f"[{len(self.hijos)} hijos]")
            for i in self.hijos:
                i.imprimir(self.datos)
        
        if self.obtenerNivel() == nivel:
            print(self.obtenerNivel() * "    ", '->', self.datos, f"[{len(self.hijos)} hijos]")

        if self.hijos:
            for i in self.hijos:
                i.imprimir(nombre_nivel, nivel)

def principal(): 
    
    raiz = Arbol("CEO")
    rrhh, ti, marketing = Arbol("RRHH"), Arbol("TI"), Arbol("MARKETING")

    rrhh.agregarHijo(Arbol("NOMAN KHAN"))
    rrhh.agregarHijo(Arbol("MIR JAFAR"))
    rrhh.agregarHijo(Arbol("FAHAD KHAN"))
    rrhh.agregarHijo(Arbol("YOUSUF SHEIKH"))

    ti.agregarHijo(Arbol("SALMAN KHAN"))
    ti.agregarHijo(Arbol("DUMBLEDORE"))
    ti.agregarHijo(Arbol("ANUSHKA SHARMA"))
    ti.agregarHijo(Arbol("THING"))

    marketing.agregarHijo(Arbol("RON WEASLY"))
    marketing.agregarHijo(Arbol("ENID"))
    marketing.agregarHijo(Arbol("TYLER"))
    marketing.agregarHijo(Arbol("XAVIER"))
    miercoles = Arbol("MIÉRCOLES")
    marketing.agregarHijo(miercoles)

    raiz.agregarHijo(rrhh)
    raiz.agregarHijo(ti)
    raiz.agregarHijo(marketing)

    raiz.imprimir()
    print("===================")
    raiz.imprimir(nombre_nivel='TI')
    print("===================")
    raiz.imprimir(nivel=1)
    print("===================")
    print(raiz.buscar("MIÉRCOLES"))
    print(raiz.obtenerRaiz())
    print(miercoles.obtenerRaiz())
    print("===================")
    print(raiz.obtenerPadre("MIÉRCOLES"))
    print(raiz.obtenerPadre("TI"))
    print(raiz.obtenerPadre("CEO"))

if __name__ == "__main__":
    principal()
