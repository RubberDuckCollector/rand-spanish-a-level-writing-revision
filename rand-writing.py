import random

requiem_questions = [
    "Describe la visita a las cuevas y explica el efecto que tuvo en Paco.",
    "¿En qué medida crees que el lector puede empatizar con Mosén Millán?",
    "Analiza cómo presenta Sender a los tres hombres ricos del pueblo. ¿Qué mensaje quiere dar al lector a través de ellos?",
    "\"En el pueblo, la religión y la superstición existen cómodamente la una al lado de la otra.\" Analiza esta afirmación y justifica tus ideas.",
    "\"Sender presenta a la gente del pueblo como gente sencilla y decente, pero al mismo tiempo como gente ignorante, casi como animales\". ¿Hasta qué punto estás de acuerdo con esta afirmación? Justifica tus ideas. Analiza el tema de la traición en la novela.",
    "Analiza cómo presenta Sender a la Iglesia Católica en la novela.",
    "\"Creer que las cosas no pueden ni deben cambiar es el mayor defecto de Mosén Millán\". Analiza esta afirmación y justifica tus ideas.",
    "\"A pesar de que Paco ha muerto, su memoria sigue muy viva\". ¿Cómo muestra *Sender* el impacto que ha tenido Paco?",
    "Analiza la actitud de los campesinos hacia la política.",
    "¿Hasta qué punto piensas que la novela es una alegoría de la lucha del pueblo español contra la fuerzas de la represión de la época? Justifica tus ideas.",
    "Analiza el uso del simbolismo en la novela.",
    "Analiza el papel de Mosén Millán en la novela. En tu opinión, ¿es culpable de la muerte de Paco o es una víctima de su situación?",
    "Paco es demasiado ingenuo para ser un héroe creíble. Muere por ideas simplistas y superficiales. ¿Estás de acuerdo? Justifica tu respuesta.",
    "Explica lo que aprendemos sobre el personaje de Paco a través de otros personajes de la novela.",
    "Explica cómo cambia la relación entre Paco y Mosén Millan a lo largo de la novela.",
    "Comenta la vida de los campesinos del pueblo. ¿Cuáles aspectos enfatiza el autor?",
    "Comenta el personaje de Mosén Millán. ¿Pienas que el autor le representa de una manera positiva o negativa?",
    "Explica la comunidad creada por Sender en la novela.",
    "Considera la relación de Mosén Millán con los diferentes grupos sociales en la obra.",
    "Explica la importancia de las constumbres y tradiciones para los campesinos en la novela.",
    "Explica los factores que conducen a la muerte a Paco.",
]


volver_questions = [
    "Analiza la impoartancia de las mujeres en la película.",
    "¿Por qué es Volver una de las películas más aclamadas?",
    "Analiza la forma idealizada en la que Almodóvar presenta a las mujeres en Volver.",
    "¿Qué responsabilidades tiene Raimunda con respecto a la muerte de Paco?",
    "Al final de la obra, las mujeres se reúnen ¿Pueden esperar un futuro mejor los personajes principales?",
    "El personaje de Raimunda desarrolla a lo largo de la película ¿Hasta qué punto estás de acuerdo?",
    "Analiza las técnicas que Almodóvar utiliza para explorar el tema de la muerte en Volver.",
    "Analiza las técnicas que Almodóvar utiliza para explorar el tema de la familia en Volver.",
    "Analiza las técnicas que Almodóvar utiliza para crear situaciones de suspense en Volver.",
    "Analiza los personajes de Sole y Raimunda. ¿Cuál de los dos te parece más fuerte?",
    "Analiza el tema de la solidaridad femenina en la película.",
    "¿Cómo son las mujeres fuertes en Volver?",
    "Analiza los contrastes entre el pueblo y la ciudad.",
    "Analiza cómo el director representa la cultura española.",
    "¿Hasta qué punto se puede decir que un conocimiento de la cultura española es necesario para entender bien la película?",
    "Uno de los temas principales en Volver es la capacidad humana de sobrevivr en situaciones difíciles. ¿Hasta qué punto desmuestran los personajes de la obra esta capacidad?",
    "Analiza el comportamiento humano y el comportamiento inhumano de los personajes en la pelicula.",
    "A pesar de la situación difícil de la familia de Raimunda, la película nos hace reír. ¿Estás de acuerdo?",
    "Analiza la representación de los hombres en la película.",
    "Analiza los tipos deferentes de amor en Volver.",
    "Analiza los temas del filme. ¿Cuál de ellos te parece más importantes?",
    "Analiza la importancia del título 'Volver'.",
    "En esta película, las mujeres tiene todo el poder. ¿Estás de acuerdo?.",
    "Analiza las razones por las que la película es tan exitosa.",
    "Analiza cómo el director mezcla los estereotipos en la película.",
]


def main():
    print("REQIUEM QUESTIONS")
    for i in range(2):
        chosen_question = random.choice(requiem_questions)
        print(f"{i+1}: {chosen_question}")
        requiem_questions.remove(chosen_question)

    print("\nVOLVER QUESTIONS")
    for i in range(2):
        chosen_question = random.choice(volver_questions)
        print(f"{i+1}: {chosen_question}")
        volver_questions.remove(chosen_question)


if __name__ == '__main__':
    main()
