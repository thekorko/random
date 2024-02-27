module Obera
    #...más cosas que ahora no interesan...
  end
  
  module Pepita
    @energia = 100
    @ciudad = Obera
  
    #...más cosas que ahora no interesan...
  end
  
  module Kiano1100
    #...más cosas que ahora no interesan...
  end
  
  module RolamotoC115
    #...más cosas que ahora no interesan...
  end
  
  module Enrique
    @celular = Kiano1100
    @dinero_en_billetera = 13
    @frase_favorita = 'la juventud está perdida'
  end
#Los objetos pueden tener múltiples atributos y al conjunto de estos atributos se lo denomina estado.

estado_pepita = %w(
  energia
  ciudad
)
  
estado_kiano1100 = %w(

)
  
estado_rolamotoC115 = %w(

) 

estado_enrique = %w(
  celular
  dinero_en_billetera
  frase_favorita 
)