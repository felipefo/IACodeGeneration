// Definindo a Entidade Base Entity
entity Entity {
    attribute Id: int
}

// Definindo a Entidade Produto
entity Produto : Entity {
    attribute Nome: string
    attribute Preco: decimal
    attribute CategoriaId: int

    // Regras de Negócio
    rule PrecoMaiorQueZero: Preco > 0
    rule NomeNaoPodeSerVazio: Nome != ""
    
    // Relação com Categoria
    relation Categoria
}

// Definindo a Entidade Categoria
entity Categoria : Entity {
    attribute Nome: string

    // Regras de Negócio
    rule NomeNaoPodeSerVazio: Nome != ""
    
    // Relação com Produtos (uma categoria pode ter vários produtos)
    relation Produtos[*]: Produto
}

// Definindo a Entidade Usuario
entity Usuario : Entity {
    attribute Nome: string
    attribute Email: string
    attribute Senha: string

    // Regras de Negócio
    rule EmailUnicoEValido: isValidEmail(Email) && isUnique(Email)
    rule SenhaMinimo8Caracteres: length(Senha) >= 8
}

// Funções Auxiliares para Regras de Negócio
function isValidEmail(email: string): boolean {
    // Implementação de validação de email
}

function isUnique(email: string): boolean {
    // Implementação de verificação de unicidade
}
