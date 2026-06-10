import { GET_CLIMA_DATA } from 'volto-v2tec-intranet/constants/ActionTypes';

export function getClimaData(location: string) {
  const path = `/@clima?localidade=${location}`;
  return {
    type: GET_CLIMA_DATA,
    request: {
      op: 'get',
      path: path,
    },
  };
}
