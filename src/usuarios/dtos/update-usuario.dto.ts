import { UsuarioPerfil } from '../usuario-perfis.enum';
import { IsString, IsEmail, IsOptional } from 'class-validator';
export class UpdateUsuarioDto {
  /*Nome*/
  @IsOptional()
  @IsString({
    message: 'Informe um nome válido',
  })
  nome: string;

  /*Username*/
  @IsOptional()
  @IsString({
    message: 'Informe um nome de usuário válido',
  })
  username: string;

  /*Email*/
  @IsOptional()
  @IsEmail(
    {},
    {
      message: 'Informe um endereço de email válido',
    },
  )
  email: string;

  /*Cargo*/
  @IsOptional()
  @IsString({
    message: 'Informe um cargo válido',
  })
  cargo: string;

  /*Perfil*/
  @IsOptional()
  perfil: UsuarioPerfil;
}
