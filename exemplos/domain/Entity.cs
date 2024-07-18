using System.Reflection;

namespace ConectaFapes.Domain.Common
{
    public class BaseEntity
    {
        public Guid Id { get; set; }
        public DateTimeOffset DateCreated { get; set; } = DateTimeOffset.Now;
        public DateTimeOffset? DateUpdated { get; set; }
        public DateTimeOffset? DateDeleted { get; set; }

        public void Update(BaseEntity entity)
        {
            foreach (PropertyInfo property in entity.GetType().GetProperties())
            {
                if (property.CanWrite && property.Name != nameof(Id) && property.Name != nameof(DateCreated))
                {
                    property.SetValue(this, property.GetValue(entity));
                }
            }

            this.DateUpdated = DateTime.Now;
        }

        public void Delete()
        {
            this.DateDeleted = DateTime.Now;
        }
    }
}
