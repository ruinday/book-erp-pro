<script setup lang='ts'>
import BookCard from './components/BookCard.vue';
import { useSwitchStore } from './stores/show';
import { get_all, del_data, put_data } from './request/api';
import { ref, onBeforeMount, reactive } from 'vue';

onBeforeMount(() => {
  get_books()
})

const books = ref([])
async function get_books() {
  const res = await get_all()
  books.value = res
}

async function del_book(id: number) {
  const res = await del_data(id)
  if (res.status === 200) {
    get_books()
  } else {
    console.log(res.error);
  }
}

const show_put = ref(false)
let book = reactive({})
const bid = ref(0)
let name = ref(book.name)
let author = ref(book.author)
let price = ref(book.price)
let publish_date = ref(book.publish_date)
let publisher = ref(book.publisher)
function show_putcard(id: number) {
  bid.value = id
  book = books.value[bid.value]
  name = ref(book.name)
  author = ref(book.author)
  price = ref(book.price)
  publish_date = ref(book.publish_date)
  publisher = ref(book.publisher)

  put_switch()
}

function put_switch() {
  show_put.value = !show_put.value
}

async function mdf_book() {
  await put_data(book.id,
    {
      'name': name.value,
      'author': author.value,
      'price': price.value,
      'publish_date': publish_date.value,
      'publisher': publisher.value
    })
  put_switch()
  get_books()
}
</script>

<template>
  <div class="container">
    <div class="top">
      <img src="/src/assets/images/favicon.ico" alt="">
      <span>图书管理系统</span>
    </div>
    <button class="btn-add" @click="useSwitchStore().show_change">新增图书</button>
    <div class="book-card" v-show="useSwitchStore().show_add">
      <BookCard></BookCard>
    </div>
    <div class="put-card" v-show="show_put">
      <p class="close" @click="put_switch">X</p>
      <p class="title">修改图书信息</p>
      <div class="bid">
        <span>图书编号：</span>
        <input type="text" class="short" :value="book.id" disabled>
      </div>
      <input type="text" class="long" placeholder="书名" v-model="name" autofocus>
      <input type="text" placeholder="作者" v-model="author">
      <input type="number" placeholder="价格" v-model="price">
      <input type="date" placeholder="出版时间" v-model="publish_date">
      <input type="text" class="long" placeholder="出版社" v-model="publisher">
      <button @click="mdf_book()">修改</button>
    </div>
    <table>
      <tr>
        <th>编号</th>
        <th>书名</th>
        <th>作者</th>
        <th>价格</th>
        <th>出版时间</th>
        <th>出版社</th>
        <th>操作</th>
      </tr>
      <tr v-for="it, index in books" :key="index">
        <td>{{ it.id }}</td>
        <td>{{ it.name }}</td>
        <td>{{ it.author }}</td>
        <td>{{ it.price }}</td>
        <td>{{ it.publish_date }}</td>
        <td>{{ it.publisher }}</td>
        <td>
          <button @click="show_putcard(index)">修改</button>
          <button class="btn-del" @click="del_book(it.id)">删除</button>
        </td>
      </tr>
    </table>
  </div>
</template>

<style lang='scss' scoped>
@import '/src/assets/main.scss';

.container {
  width: 1000px;
  margin: 10vh auto 0 auto;
  border-radius: 6px;
  padding: 30px;
  background: #fff;

  .top {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 10px 0 20px 0;

    img {
      width: 35px;
      height: 35px;
      margin-right: 20px;
    }

    span {
      font-size: 24px;
    }
  }

  .btn-add {
    width: 70px;
    height: 26px;
    border: 0;
    border-radius: 4px;
    color: #fff;
    font-size: 14px;
    background: $mcolor;
    cursor: pointer;
  }

  .book-card {
    position: fixed;
    top: calc((100vh - 400px)* 0.35);
    left: calc((100vw - 400px)* 0.5);
  }

  .put-card {
    width: 400px;
    border-radius: 6px;
    background: #fff;
    padding: 20px;
    box-shadow: 0 0 5px;
    display: flex;
    flex-direction: column;
    position: fixed;
    top: calc((100vh - 400px)* 0.18);
    left: calc((100vw - 400px)* 0.5);

    p.close {
      position: absolute;
      top: 0px;
      right: 20px;
      cursor: pointer;
    }

    p.title {
      font-size: 20px;
      text-align: center;
    }

    .bid {

      span {
        font-size: 14px;
      }

      .short {
        width: 20px;
        border: 0;
        background: #fff;
      }
    }

    input {
      width: 100%;
      height: 30px;
      margin: 10px 0;
      border: $border;
      border-radius: 4px;

      &:focus {
        outline: none;
      }
    }



    button {
      width: 100%;
      height: 32px;
      border: 0;
      color: #fff;
      border-radius: 4px;
      background: $bgcolor;
      margin: 20px 0 40px 0;
    }
  }

  table {
    width: 100%;
    margin: 20px 0;
    border-top: $border;
    border-bottom: $border;

    tr {
      th {
        font-size: 15px;
        font-weight: 500;
        text-align: center;
        line-height: 30px;
        border-bottom: $border;
      }


      td {
        color: $fcolor1;
        font-size: 14px;
        text-align: center;

        button {
          width: 40px;
          height: 25px;
          font-size: 12px;
          margin-left: 10px;
          border: 0;
          border-radius: 4px;

          &:hover {
            color: #fff;
            background: $bgcolor;
          }
        }

        .btn-del {
          color: $redcolor;
        }
      }
    }

  }
}
</style>
