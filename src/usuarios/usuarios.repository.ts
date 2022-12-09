import { EntityRepository, Repository } from 'typeorm';
import { Usuario } from './usuario.entity';
import { CreateUsuarioDto } from './dtos/create-usuario.dto';
import { UsuarioPerfil } from './usuario-perfis.enum';
import * as bcrypt from 'bcrypt';
import * as crypto from 'crypto';
import {
  ConflictException,
  InternalServerErrorException,
} from '@nestjs/common';

@EntityRepository(Usuario)
export class UsuarioRepository extends Repository<Usuario> {
  async createUser(
    createUsuarioDto: CreateUsuarioDto,
    role: UsuarioPerfil,
  ): Promise<Usuario> {
    const { email, nome, username, cargo, password } = createUsuarioDto;

    const user = this.create();
    user.email = email;
    user.nome = nome;
    user.perfil = role;
    user.username = username;
    user.cargo = cargo;
    user.confirmationToken = crypto.randomBytes(32).toString('hex');
    user.salt = await bcrypt.genSalt();
    user.password = await this.hashPassword(password, user.salt);
    try {
      await user.save();
      delete user.password;
      delete user.salt;
      return user;
    } catch (error) {
      if (error.code.toString() === '23505') {
        throw new ConflictException('Endereço de email já está em uso');
      } else {
        throw new InternalServerErrorException(
          'Erro ao salvar o usuário no banco de dados',
        );
      }
    }
  }
  private async hashPassword(password: string, salt: string): Promise<string> {
    return bcrypt.hash(password, salt);
  }
}
