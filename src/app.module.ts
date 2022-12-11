import { Module } from '@nestjs/common';
import configuration from './configs/configuration';
import { ConfigModule } from '@nestjs/config';
import { UsuariosModule } from './usuarios/usuarios.module';
import { TypeOrmModule } from '@nestjs/typeorm';

@Module({
  imports: [
    ConfigModule.forRoot({ load: [configuration] }),
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'schedula_user_db',
      port: 5432,
      username: 'postgres',
      password: 'postgres',
      database: 'schedula_user',
      entities: [__dirname + '/../**/*.entity.{js,ts}'],
      synchronize: true,
    }),
    UsuariosModule,
  ],
  controllers: [],
  providers: [],
})
export class AppModule {}
