interface AccountService
{
    public function createAccount($username, $password);
    public function updateAccount($username, $password);
    public function deleteAccount($username);
}

class UserAccount implements AccountService
{
    public function createAccount($username, $password)
    {
        // lógica para criar conta
    }

    public function updateAccount($username, $password)
    {
        // lógica para atualizar conta
    }

    public function deleteAccount($username)
    {
        // lógica para deletar conta
    }
}
