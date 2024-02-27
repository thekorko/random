##Como verás, tenemos distintos grados de similitud en el código:

energia es igual para ambas clases, porque sólo devuelve la energía;
Una parte de atacar! coincide: en la que el zombi recibe_danio!, pero en Aliado reduce energía y en Sobreviviente no;
beber! es diferente para ambas clases.
Último esfuerzo: definí una clase abstracta Persona que agrupe el comportamiento que se repite y hacé que las clases Sobreviviente y Aliado hereden de ella.


##En Sobreviviente y Aliado solo deberán estar definidos los métodos que son particulares de ellas. Y por las dudas ¡no te olvides de super!
##
class Persona

    def energia
      @energia
    end
    
    def atacar!(zombi, danio)
      zombi.recibir_danio! danio
    end
  end
  #Un Sobreviviente es persona, hereda de persona
  class Sobreviviente < Persona
    def initialize
      @energia = 1000
    end
    
    def beber!
      @energia *= 1.25
    end
  
  end
  #Un Aliado es persona, hereda de persona
  class Aliado < Persona
    def initialize
      @energia = 500
    end
  
    def beber!
      @energia *= 1.10
    end
  
    def atacar!(zombi, danio)
      super
      @energia *= 0.95
    end
  end