# TP1 — Modelagem do sistema de biblioteca

Minhas respostas ao TP1: análise de uma tabela única mal estruturada e proposta de modelo relacional. As partes em SQL (CREATE TABLE) estão no notebook do Deepnote linkado no README.

## Exercício 1

A tabela criada pelo estagiário mistura três coisas bem diferentes na mesma estrutura. A primeira é o Livro que representa o acervo físico da biblioteca, guardando informações permanentes do exemplar como título, autor, ISBN e marcas de uso, ele existe no sistema independentemente de estar emprestado ou não. A segunda é o Leitor que representa o usuário cadastrado que tem permissão para retirar livros, identificado pelo nome, e-mail, curso, telefone e data de cadastro. A terceira é o Empréstimo que representa o evento que une livro e leitor num determinado momento registrando as datas de retirada, limite e devolução, ele nasce quando o livro é retirado e se encerra quando é devolvido. O grande problema de juntar tudo numa tabela só é que os dados do livro ficam repetidos em cada linha toda vez que ele é emprestado para alguém diferente, o que gera redundância e confusão.

## Exercício 2

Dentro das entidades temos os seguintes atributos começando pelo livro: livro_titulo é um texto que armazena o título completo do livro, autor é um texto que guarda o nome de quem escreveu a obra, isbn é um texto pois, apesar de ser composto apenas por números na tabela original, representa um código identificador único e não deve ser utilizado em operações matemáticas, marcas_uso é um texto que registra observações sobre o estado de conservação do exemplar. Leitor: leitor_nome é um texto que armazena o nome completo do leitor cadastrado, leitor_email é um texto que guarda o endereço de e-mail usado para contato com o leitor, leitor_curso é um texto que indica o curso ao qual o leitor está vinculado, telefone_leitor é um texto pois, embora apareça como número na tabela original, pode conter formatação, DDD e não é utilizado para cálculos, representando apenas um meio de contato, data_cadastro é uma data que registra quando o leitor foi adicionado ao sistema. Empréstimo: data_emprestimo é uma data que marca o dia em que o livro foi retirado pelo leitor, data_limite é uma data que define o prazo máximo para que o livro seja devolvido, data_devolucao é uma data que registra o dia em que o livro foi efetivamente devolvido, podendo estar vazia caso o livro ainda não tenha sido devolvido.

## Exercício 3

Para a entidade Livro, um bom identificador seria o ISBN, pois ele é um código internacional único para cada obra. Portanto, dois livros diferentes não devem possuir o mesmo ISBN, sendo adequado como identificador da tabela porque garante unicidade para cada registro. Porém, vale observar que o ISBN identifica a obra, não necessariamente o exemplar físico. Caso a biblioteca possua mais de um exemplar do mesmo livro, o ideal seria criar um identificador próprio gerado pelo sistema, como id_livro. Título e autor não servem pois podem se repetir, já que um mesmo autor pode ter vários livros e títulos podem existir em diferentes edições. O campo marcas_uso também não serve, pois é uma informação variável, opcional e não identifica o livro de forma única. Para a entidade Leitor, o e-mail é um bom identificador, pois dois usuários não devem possuir o mesmo endereço no sistema. Nome e curso não servem porque podem se repetir entre diferentes pessoas. O telefone também não é ideal, pois nem todos os leitores possuem esse dado preenchido

## Exercício 4

Regra 1: Um livro só pode ter um empréstimo ativo por vez, um mesmo livro não pode estar emprestado para dois leitores ao mesmo tempo, enquanto a data_devolucao de um empréstimo estiver em aberto, o sistema não deve permitir um novo empréstimo para aquele mesmo livro, garantindo assim o controle correto da disponibilidade do acervo, essa regra envolve as entidades Livro e Empréstimo e é fundamental para evitar inconsistências nos dados.

Regra 2: Todo empréstimo deve estar vinculado a um leitor e a um livro cadastrados, não pode existir um empréstimo sem que o leitor e o livro correspondentes estejam previamente cadastrados no sistema, garantindo que todas as operações sejam rastreáveis e consistentes. Essa regra envolve as entidades Leitor, Livro e Empréstimo e evita a existência de registros incompletos ou sem referência no banco de dados.

## Exercício 5

A primeira tabela a ser implementada será a tabela Livro, pois representa um objeto permanente do sistema. Seus atributos são: isbn é um texto que representa o código internacional de identificação da obra; livro_titulo é um texto que armazena o título completo da obra; autor é um texto que guarda o nome do autor; marcas_uso é um texto que registra observações sobre o estado físico do exemplar, como capa desgastada, páginas amareladas ou anotações.

## Exercício 6 e Exercício 7

_Resposta em SQL no notebook do Deepnote._

## Exercício 8

A segunda tabela a ser implementada será a tabela Leitor, pois representa outro objeto permanente do sistema da biblioteca. Seus atributos são: leitor_email, que é um texto e armazena o e-mail do leitor, podendo ser usado para identificá-lo no sistema; leitor_nome, que é um texto e guarda o nome completo do leitor cadastrado; leitor_curso, que é um texto e indica o curso ao qual o leitor está vinculado; telefone_leitor, que é um texto e armazena o telefone do leitor, podendo ficar vazio caso ele não tenha informado esse dado e data_cadastro, que é uma data e registra quando o leitor foi cadastrado no sistema.

## Exercício 9 e Exercício 10

_Resposta em SQL no notebook do Deepnote._

## Exercício 11

A terceira tabela será a tabela Emprestimo, pois representa o evento em que um leitor retira um livro da biblioteca por um período determinado. Seus atributos são: isbn, que é um texto e indica qual livro foi emprestado; leitor_email, que é um texto e indica qual leitor realizou o empréstimo; data_emprestimo, que é uma data e registra o dia em que o livro foi retirado; data_limite, que é uma data e define o prazo máximo para devolução; e data_devolucao, que é uma data e registra quando o livro foi devolvido, podendo ficar vazia caso o empréstimo ainda esteja em aberto.

## Exercício 12

_Resposta em SQL no notebook do Deepnote._

## Exercício 13

Para resolver o problema de identificação única de cada ocorrência, pode ser adicionado o atributo id_emprestimo, que será um número inteiro e funcionará como chave primária da tabela. Esse campo é necessário pois um mesmo leitor pode realizar vários empréstimos e um mesmo livro pode ser emprestado várias vezes ao longo do tempo, tornando impossível diferenciar cada registro sem um identificador próprio. (o SQL está no notebook do Deepnote)

## Exercício 14

O controle de pendências deve ser armazenado em uma tabela separada porque representa uma nova ocorrência do sistema, ligada aos casos em que um livro é devolvido fora do prazo. Essa nova tabela passa a registrar informações como qual empréstimo gerou a pendência, quando ela foi registrada, qual valor será cobrado e se a situação já foi regularizada ou não. Essas informações não devem ficar misturadas diretamente na tabela de empréstimos, pois nem todo empréstimo gera pendência. Separar esses dados melhora a organização do banco, evita campos desnecessários e facilita a consulta das pendências em aberto.

## Exercício 15

A nova tabela será chamada Pendencia, pois representa uma pendência financeira ou administrativa gerada por atraso na devolução. Seus atributos são: id_pendencia, que é um número inteiro e identifica cada pendência de forma única; id_emprestimo, que é um número inteiro e indica qual empréstimo gerou a pendência; data_registro, que é uma data e informa quando a pendência foi registrada no sistema; valor_cobranca, que é um número decimal e armazena o valor da cobrança associada ao atraso; e regularizada, que é um booleano e informa se a pendência já foi resolvida ou não.

## Exercício 16

_Resposta em SQL no notebook do Deepnote._
