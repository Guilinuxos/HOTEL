CREATE DATABASE hotelaria;
USE hotelaria;

CREATE TABLE hospedes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    cpf VARCHAR(14) UNIQUE
);

CREATE TABLE quartos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(10) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    valor_diaria DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,

    hospede_id INT,
    quarto_id INT,

    data_entrada DATE NOT NULL,
    data_saida DATE NOT NULL,

    FOREIGN KEY (hospede_id)
    REFERENCES hospedes(id),

    FOREIGN KEY (quarto_id)
    REFERENCES quartos(id)
);

-- =========================
-- POVOAMENTO DA TABELA HOSPEDES
-- =========================

INSERT INTO hospedes (nome, email, telefone, cpf) VALUES
('Ana Silva', 'ana.silva@email.com', '(19) 99999-1111', '123.456.789-01'),
('Carlos Souza', 'carlos.souza@email.com', '(19) 98888-2222', '234.567.890-12'),
('Mariana Costa', 'mariana.costa@email.com', '(19) 97777-3333', '345.678.901-23'),
('João Pereira', 'joao.pereira@email.com', '(19) 96666-4444', '456.789.012-34'),
('Fernanda Lima', 'fernanda.lima@email.com', '(19) 95555-5555', '567.890.123-45');

-- =========================
-- POVOAMENTO DA TABELA QUARTOS
-- =========================

INSERT INTO quartos (numero, tipo, valor_diaria, status) VALUES
('101', 'Solteiro', 120.00, 'Disponível'),
('102', 'Casal', 180.00, 'Ocupado'),
('103', 'Luxo', 350.00, 'Disponível'),
('104', 'Suíte', 500.00, 'Manutenção'),
('105', 'Família', 280.00, 'Disponível');

-- =========================
-- POVOAMENTO DA TABELA RESERVAS
-- =========================

INSERT INTO reservas (hospede_id, quarto_id, data_entrada, data_saida) VALUES
(1, 2, '2026-05-10', '2026-05-15'),
(2, 1, '2026-05-12', '2026-05-14'),
(3, 3, '2026-05-20', '2026-05-25'),
(4, 5, '2026-06-01', '2026-06-07'),
(5, 2, '2026-06-10', '2026-06-12');
