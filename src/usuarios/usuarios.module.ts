import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UsuariosService } from './usuarios.service';
import { Usuario } from './usuario.entity';
import { UsuariosController } from './usuarios.controller';

@Module({
  imports: [TypeOrmModule.forFeature([Usuario])],
  providers: [UsuariosService],
  controllers: [UsuariosController],
})
export class UsuariosModule {}
