import {
  Injectable,
  UnprocessableEntityException,
  ConflictException,
  InternalServerErrorException,
} from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { CreateUsuarioDto } from './dtos/create-usuario.dto';
import { Usuario } from './usuario.entity';
import { UsuarioPerfil } from './usuario-perfis.enum';
import { Repository } from 'typeorm';
import * as bcrypt from 'bcrypt';
import * as crypto from 'crypto';

@Injectable()
export class UsuariosService {
  constructor(
    @InjectRepository(Usuario)
    private usuarioRepository: Repository<Usuario>,
  ) {}

  async createUsuario(createUsuarioDto: CreateUsuarioDto): Promise<Usuario> {
    const { email, nome, username, perfil, cargo, password } = createUsuarioDto;
    const user = this.usuarioRepository.create();
    user.email = email;
    user.nome = nome;
    user.perfil = UsuarioPerfil[perfil];
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
