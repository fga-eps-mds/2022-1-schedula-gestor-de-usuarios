// Importa decorators adicionais para validação de campos.

// Possibilidade de usar o decorator @Matches para aumentar a segurança das senhas
import { IsEmail, IsNotEmpty, MaxLength, MinLength } from 'class-validator';

export class CreateUsuarioDto {
  /*Email*/

  @IsNotEmpty({
    message: 'Informe um endereço de email',
  })
  @IsEmail(
    {},
    {
      message: 'Informe um endereço de email válido',
    },
  )
  @MaxLength(200, {
    message: 'O endereço de email deve ter menos de 200 caracteres',
  })
  email: string;

  /*Nome*/

  @IsNotEmpty({
    message: 'Informe o nome do usuário',
  })
  @MaxLength(200, {
    message: 'O nome deve ter menos de 200 caracteres',
  })
  nome: string;

  /*Username*/

  @IsNotEmpty({
    message: 'Informe o nome do usuário',
  })
  @MaxLength(50, {
    message: 'O nome deve ter menos de 50 caracteres',
  })
  username: string;

  /*Cargo*/

  @IsNotEmpty({
    message: 'Informe um cargo',
  })
  @MaxLength(200, {
    message: 'O cargo deve ter menos de 200 caracteres',
  })
  cargo: string;

  /*Perfil*/

  @IsNotEmpty({
    message: 'Informe um perfil de usuário',
  })
  perfil: string;

  /*Senha*/

  @IsNotEmpty({
    message: 'Informe uma senha',
  })
  @MinLength(6, {
    message: 'A senha deve ter no mínimo 6 caracteres',
  })
  password: string;
}
