import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  Post,
  Put,
  Patch,
  ValidationPipe,
} from '@nestjs/common';
import { CreateUsuarioDto } from './dtos/create-usuario.dto';
import { UsuariosService } from './usuarios.service';
import { ReturnUsuarioDto } from './dtos/return-usuario.dto';
import { UpdateUsuarioDto } from './dtos/update-usuario.dto';
import { AuthGuard } from '@nestjs/passport';

@Controller('usuarios')
export class UsuariosController {
  constructor(private usuariosService: UsuariosService) {}

  @Post()
  async createUsuario(
    @Body(ValidationPipe) createUsuarioDto: CreateUsuarioDto,
  ): Promise<ReturnUsuarioDto> {
    const usuario = await this.usuariosService.createUsuario(createUsuarioDto);
    return {
      usuario,
      message: 'Usuario cadastrado com sucesso',
    };
  }
  @Get(':id')
  async findUsuarioById(@Param('id') id): Promise<ReturnUsuarioDto> {
    const usuario = await this.usuariosService.findUsuarioById(id);
    return {
      usuario,
      message: 'Usuário encontrado',
    };
  }
  @Patch(':id')
  async updateUsuario(
    @Body(ValidationPipe) updateUsuarioDto: UpdateUsuarioDto,
    @Param('id') id: string,
  ) {
    return this.usuariosService.updateUsuario(updateUsuarioDto, id);
  }
  @Delete(':id')
  async deleteUsuario(@Param('id') id: string) {
    await this.usuariosService.deleteUsuario(id);
    return {
      message: 'Usuário removido com sucesso',
    };
  }
}
