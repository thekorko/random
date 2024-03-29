module Obera
  def self.kilometro
    1040
  end
  def self.distancia_a(destino)
    (self.kilometro - destino.kilometro).abs
  end
end

module Iruya
  def self.kilometro
    1710
  end 
  def self.distancia_a(destino)
    (self.kilometro - destino.kilometro).abs
  end
end

module BuenosAires
  def self.kilometro
    0
  end 
  def self.distancia_a(destino)
    (self.kilometro - destino.kilometro).abs
  end
end

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
  def self.gastar_energia!(destino)
    @energia -= @ciudad.distancia_a(destino)/ 2
  end
end