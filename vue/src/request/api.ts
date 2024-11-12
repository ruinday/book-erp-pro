import { service } from './http'

export function get_all() {
  return service({
    url: '/books',
    method: 'get',
  })
}

export function add_data(data: object) {
  return service({
    url: '/books',
    method: 'post',
    data,
  })
}

export function get_one(bid: number) {
  return service({
    url: `/books/${bid}`,
    method: 'get',
  })
}

export function put_data(bid: number, data: object) {
  return service({
    url: `/books/${bid}`,
    method: 'put',
    data,
  })
}

export function del_data(bid: number) {
  return service({
    url: `/books/${bid}`,
    method: 'delete',
  })
}

// 使用已封装好的axios
// import { get_data, update_data } from '@/request/api'

// export default {
//   methods: {
//     async fetchUserInfo() {
//       try {
//         const response = await getUserInfo({ id: 1 })
//         console.log(response)
//       } catch (error) {
//         console.error(error)
//       }
//     },
//     async updateUser() {
//       try {
//         const response = await updateUserInfo({ name: 'New Name' })
//         console.log(response)
//       } catch (error) {
//         console.error(error)
//       }
//     },
//   },
// }
