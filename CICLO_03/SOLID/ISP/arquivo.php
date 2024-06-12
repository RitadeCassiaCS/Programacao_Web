interface EmailServiceInterface
{
    public function sendWelcomeEmail($email);
}

interface ActivityLoggerInterface
{
    public function logActivity($activity);
}

class EmailService implements EmailServiceInterface
{
    public function sendWelcomeEmail($email)
    {
        // lógica para enviar e-mail de boas-vindas
    }
}

class ActivityLogger implements ActivityLoggerInterface
{
    public function logActivity($activity)
    {
        // lógica para registrar atividade
    }
}
