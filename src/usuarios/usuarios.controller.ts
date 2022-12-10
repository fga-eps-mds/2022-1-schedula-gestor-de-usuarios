import { Controller, Post, Body, ValidationPipe } from '@nestjs/common';
import { CreateUsuarioDto } from './dtos/create-usuario.dto';
import { UsuariosService } from './usuarios.service';
import { ReturnUsuarioDto } from './dtos/return-usuario.dto';

@Controller('usuarios')
export class UsuariosController {
  constructor(private usuariosService: UsuariosService) {}

  @Post()
  async createUsuarioAdmin(
    @Body(ValidationPipe) createUsuarioDto: CreateUsuarioDto,
  ): Promise<ReturnUsuarioDto> {
    const usuario = await this.usuariosService.createUsuarioAdmin(
      createUsuarioDto,
    );
    return {
      usuario,
      message: 'Administrador cadastrado com sucesso',
    };
  }
}
