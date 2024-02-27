module Jor
    @plato_del_dia
    def self.plato_del_dia=(plato)
      @plato_del_dia = plato
    end
  
    def self.picantear!
      @plato_del_dia.sumar_ajies=(5)
    end
  
  end
  
  module Luchi
  
    def self.suavizar! (plato, numero)
      if(plato.cantidad_ajies<10)
        plato.restar_ajies=(numero)
      elsif(plato.cantidad_ajies>10)
        plato.descartar_la_salsa!
      end
    end
  end
  
  module Fideos
  
    @ajies = 0
  
    def self.picantes?
      @ajies>2
    end
  
    def self.sumar_ajies=(cantidad)
      @ajies += cantidad
    end
  
    def self.restar_ajies=(cantidad)
      @ajies -= cantidad
    end
  
    def self.cantidad_ajies
      @ajies
    end
  
    def self.descartar_la_salsa!
      @ajies = 0
    end
  
  end