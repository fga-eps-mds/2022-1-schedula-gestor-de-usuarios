import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  Post,
  Put,
  ValidationPipe,
} from '@nestjs/common';
import { CreateUsuarioDto } from './dtos/create-usuario.dto';
import { UsuariosService } from './usuarios.service';
import { ReturnUsuarioDto } from './dtos/return-usuario.dto';
import { get } from 'http';

@Controller('usuarios')
export class UsuariosController {
  constructor(private usuariosService: UsuariosService) {}

  @Post()
  async createUsuarioAdmin(
    @Body(ValidationPipe) createUsuarioDto: CreateUsuarioDto,
  ): Promise<ReturnUsuarioDto> {
    const usuario = await this.usuariosService.createUsuario(createUsuarioDto);
    return {
      usuario,
      message: 'Administrador cadastrado com sucesso',
    };
  }
}
