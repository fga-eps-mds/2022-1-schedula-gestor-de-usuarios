import { Module } from '@nestjs/common';
import configuration from './configs/configuration';
import { ConfigModule } from '@nestjs/config';
import { UsuariosModule } from './usuarios/usuarios.module';

@Module({
  imports: [ConfigModule.forRoot({ load: [configuration] }), UsuariosModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
