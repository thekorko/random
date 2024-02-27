class Colectivo < MedioDeTransporte
    def initialize
      @combustible = 100
      @pasajeros = 0
    end
  
    def recorrer!(kilometros)
      @combustible -= kilometros*2
    end
    def cargar_combustible!(litros)
      super
      @pasajeros = 0
    end
    
    def entran?(personas)
      true
    end
  end