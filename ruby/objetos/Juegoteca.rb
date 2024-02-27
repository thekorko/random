module CarlosDuty
  @cantidad_logros = 0

  def self.violento?
    true
  end

  def self.dificultad
    30 - @cantidad_logros * 0.5
  end

  def self.jugar!(un_tiempo)
    if(un_tiempo>=2)
      @cantidad_logros += 1
    end
  end
end

module TimbaElLeon
  @dificultad = 25
  def self.violento?
    false
  end

  def self.dificultad
    @dificultad
  end

  def self.jugar!(un_tiempo)
      @dificultad += un_tiempo
  end
end

module Metroide
  @nivel_espacial = 3

  def self.violento?
    @nivel_espacial>5
  end

  def self.dificultad
    100
  end

  def self.jugar!(un_tiempo)
    @nivel_espacial += 1
  end
end

module Juegoteca
  @juegos = [CarlosDuty,TimbaElLeon,Metroide]
  @puntos = 0
  def self.juegos
    @juegos
  end

  def self.puntos
    @puntos
  end
  def self.sumar_puntos=(cantidad)
    @puntos += cantidad
  end

  def self.adquirir_juego!(un_juego)
    juegos.push (un_juego)
    self.sumar_puntos=(150)
  end

  def self.borrar_juego!(un_juego)
    juegos.delete (un_juego)
  end

  def self.completa?
    (juegos.size>5 && puntos>1000)
  end
  #hola
  def self.juego_recomendable?(un_juego)
    (!juegos.include?(un_juego) && un_juego.violento?)
  end

end