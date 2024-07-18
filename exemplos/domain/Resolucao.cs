
//Inicio:Resolucao.cs
﻿using ConectaFapes.Domain.Common;
using ConectaFapes.Domain.Validation;

namespace ConectaFapes.Domain.Entities.CadastroModalidadesBolsas
{
    public class Resolucao : BaseEntity
    {
        public int Numero { get; set; }
        public DateTimeOffset Data { get; set; }
        public string Ementa { get; set; } = String.Empty;
        public string Link { get; set; } = String.Empty;
        public ICollection<VersaoModalidade> VersaoModalidadesBolsas { get; } = [];

        public Resolucao() { }

        public Resolucao(int numero, DateTimeOffset data, string ementa, string link)
        {
            var validationErrors = ResolucaoValidation(numero, data, ementa, link);

            if (validationErrors.Count > 0)
            {
                throw new DomainValidationException(validationErrors);
            }

            Numero = numero;
            Data = data;
            Ementa = ementa;
            Link = link;
        }

        public bool PossuiModalidades()
        {
            return (VersaoModalidadesBolsas.Count() <= 0 || VersaoModalidadesBolsas == null) ? false : true;
        }

        private List<string> ResolucaoValidation(int numero, DateTimeOffset data, string ementa, string link)
        {
            var errors = new List<string>();

            if (numero < 0) errors.Add("O número da resolução não pode ser negativo");
            if (string.IsNullOrEmpty(ementa)) errors.Add("A ementa da resolução não pode ser vazia");
            if (string.IsNullOrEmpty(link)) errors.Add("O link da resolução não pode ser vazia");

            return errors;
        }

        public void AdicionarVersaoModalidade(VersaoModalidade VersaoModalidade)
        {
            VersaoModalidadesBolsas.Add(VersaoModalidade);
        }
    }
}


//Fim:Resolucao.cs
