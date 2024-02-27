  #clase Aliado
class Aliado
    def initialize
      @energia = 500
    end
  
    def energia
      @energia
    end
  
    def beber!
      @energia += @energia*10/100
    end
  
    def atacar!(zombie, danio)
      zombie.recibir_danio!(danio)
      @energia -= @energia*5/100
    end
  
    def ataque_masivo!(zombis)
      zombis.each { |zombi| atacar!(zombi, 20) }
      @energia /= 2
    end
  end
  #clase Sobreviviente

  class Sobreviviente
    def initialize
      @energia = 1000
    end
  
    def energia
      @energia
    end
  
    def beber!
      @energia += @energia*25/100
    end
  
    def atacar!(zombie, danio)
      zombie.recibir_danio!(danio)
    end
  
    def ataque_masivo!(zombis)
      zombis.each { |zombi| atacar!(zombi, 15) }
      @energia /= 2
    end
  end

  #Zombi
  class Zombi
    def initialize(puntos)
      @salud = puntos
    end
  
    def salud
      @salud
    end
  
    def sabe_correr?
      false
    end
    
    def sin_vida?
      self.salud==0
    end
  
    def gritar
      "¡agrrrg!"
    end
  
    def recibir_danio!(cant)
      @salud=[@salud-=cant*2,0].max
    end
  end
  #super sombi
  class SuperZombi
    def initialize(puntos)
      @salud = puntos
    end
  
    def salud
      @salud
    end
  
    def sabe_correr?
      true
    end
  
    def regenerarse!
      @salud=100
    end
  
    def sin_vida?
      self.salud==0
    end
  
    def gritar
      "¡agrrrg!"
    end
  
    def recibir_danio!(cant)
      @salud=[@salud-=cant*3,0].max
    end
  end
