class UserAccountService
{
    private $accountService;
    private $emailService;
    private $activityLogger;

    public function __construct(AccountService $accountService, EmailServiceInterface $emailService, ActivityLoggerInterface $activityLogger)
    {
        $this->accountService = $accountService;
        $this->emailService = $emailService;
        $this->activityLogger = $activityLogger;
    }

    public function createAccount($username, $password, $email)
    {
        $this->accountService->createAccount($username, $password);
        $this->emailService->sendWelcomeEmail($email);
        $this->activityLogger->logActivity("Created account for $username");
    }
}
