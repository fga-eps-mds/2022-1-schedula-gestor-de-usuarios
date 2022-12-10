import { DataSource } from 'typeorm';
import { ConfigService } from '@nestjs/config';
import { Usuario } from './src/usuarios/usuario.entity';

const configService = new ConfigService();

export default new DataSource({
  type: 'postgres',
  host: 'localhost',
  port: 5105,
  username: 'postgres',
  password: 'postgres',
  database: 'postgres',
  entities: ['./src/**/*.entity.ts'],
  synchronize: true,
});
