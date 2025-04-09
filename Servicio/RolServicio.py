from Dtos.RolDTO import RolDTO
from Repositorios.RolRepositorio import RolRepositorio

repositorio =RolRepositorio();

class ServiceCuentas:
       
    def insertar(self, rolDTO: RolDTO) -> RolDTO:
        newRolDTO: RolDTO = RolDTO();
        newRolDTO=repositorio.Guardar(rolDTO);
        return newRolDTO;


    def ConsultarRoles(self) -> list[RolDTO]:
        lista: list = [];
        listaRolDTO: list[RolDTO] = [];
        lista=repositorio.ListarRoles();

        for roles in lista:
            newRolDTO: RolDTO = RolDTO();
            newRolDTO.SetId(roles[0]);
            newRolDTO.SetDescripcion(roles[1]);
            listaRolDTO.append(newRolDTO);
        return listaRolDTO;