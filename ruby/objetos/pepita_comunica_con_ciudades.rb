#biblioteca
module Obera
    def self.kilometro
      1040
    end
  end
  
  module Iruya
    def self.kilometro
      1710
    end  
  end
  
  module BuenosAires
    def self.kilometro
      0
    end  
  end
#Porque un pajaro  es responsable de calcular la distancia entre dos ciudades?
module Pepita
    @energia = 1000
    @ciudad = Obera
  
    def self.energia
      @energia 
    end
  
    def self.ciudad
      @ciudad
    end
  
    def self.cantar!
      'pri pri pri'
    end
  
    def self.comer_lombriz!
      @energia += 20
    end
  
    def self.volar_en_circulos!
      @energia -= 10
    end
  
    def self.volar_hacia!(destino)
      self.gastar_energia!(destino)
      @ciudad = destino
    end
    def self.distancia_a(destino)
      (@ciudad.kilometro - destino.kilometro).abs
    end
    def self.gastar_energia!(destino)
      @energia -= self.distancia_a(destino)/ 2
    end
  end
