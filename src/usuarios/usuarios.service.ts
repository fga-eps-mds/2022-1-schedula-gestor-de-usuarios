import { Injectable, UnprocessableEntityException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { UsuarioRepository } from './usuarios.repository';
import { CreateUsuarioDto } from './dtos/create-usuario.dto';
import { Usuario } from './usuario.entity';
import { UsuarioPerfil } from './usuario-perfis.enum';

@Injectable()
export class UsuariosService {
  constructor(
    @InjectRepository(UsuarioRepository)
    private usuarioRepository: UsuarioRepository,
  ) {}

  async createUsuarioAdmin(
    createUsuarioDto: CreateUsuarioDto,
  ): Promise<Usuario> {
    if (createUsuarioDto.password != createUsuarioDto.passwordConfirmation) {
      throw new UnprocessableEntityException('As senhas não conferem');
    } else {
      return this.usuarioRepository.createUser(
        createUsuarioDto,
        UsuarioPerfil.ADMIN,
      );
    }
  }
}
