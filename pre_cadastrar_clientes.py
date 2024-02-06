from django.core.management import BaseCommand
from .transacao.models import Cliente

class Command(BaseCommand):
    help = "Pré-cadastra cinco clientes para testes da API."

    def handle(self, *args, **options):
        clientes = [
            {
                "id": 1,
                "limite": 10000000,
                "saldo": 0,
            },
            {
                "id": 2,
                "limite": 8000000,
                "saldo": 0,
            },
            {
                "id": 3,
                "limite": 10000000,
                "saldo": 0,
            },
            {
                "id": 4,
                "limite": 10000000,
                "saldo": 0,
            },
            {
                "id": 5,
                "limite": 5000000,
                "saldo": 0,
            },
        ]

        Cliente.objects.bulk_create([Cliente(**cliente) for cliente in clientes])

        self.stdout.write(self.style.SUCCESS("Clientes pré-cadastrados com sucesso!"))

if __name__ == "__main__":
    Command().handle()