import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UsuarioRepository } from './usuarios.repository';
import { UsuariosService } from './usuarios.service';
import { UsuariosController } from './usuarios.controller';

@Module({
  imports: [TypeOrmModule.forFeature([UsuarioRepository])],
  providers: [UsuariosService],
  controllers: [UsuariosController],
})
export class UsuariosModule {}
