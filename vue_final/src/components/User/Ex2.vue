<template>
  <div>
    <el-col :span="5">
    <p >请计算出结果并填写在下方(保留两位小数):</p>
      <p >并联1uF电容的功率因数:</p>
    <el-input v-model = "uf_1" type = "primary" id = "uf_1" ></el-input>
    <p >并联2.2uF电容的功率因数:</p>
    <el-input v-model = "uf_2" type = "primary" id = "uf_2" ></el-input>
    <p >并联4.7uF电容的功率因数:</p>
    <el-input v-model = "uf_3" type = "primary" id = "uf_3" ></el-input></el-col>
    <el-button type="primary" id="submit" icon="el-icon-d-arrow-right" @click="submit(uf_1,uf_2,uf_3)">submit</el-button>
  </div>
</template>

<script>
  export default {
    name: "score",
    data() {
      return {
        uf_1: "",
        uf_2: "",
        uf_3: "",
        score: '0',
        count: 0,
        formLabelWidth: "100px"
      };
    },
    created() {

    },
    methods: {
      submit(uf_1, uf_2, uf_3) {
        this.count=0
        if(uf_1==='0.56')
          this.count += 1
        if(uf_2==='0.76')
          this.count += 1
        if(uf_3==='0.91')
          this.count += 1
        if(this.count===1)
          this.score='33'
        else if(this.count===2)
          this.score='66'
        else if(this.count===3)
          this.score='100'
        this.$axios
          .get(this.HOME + "/api/ex_score", {
            params: {
              eid: '3',
              uloginid: this.Global.loginid,
              uscore: this.score,
            }
          })
        this.$router.push({ path: "/User/Experiment" });
    }}
  };
</script>

<style lang="scss" scoped>
  #submit{
    position: absolute;
    top: 330px;
    left: 10px;
  }
  .button {
    background: transparent;
    color: transparent;
    position: absolute;
    margin-top: 500px;
    margin-bottom: 500px;
    margin-left: 45%;
    padding-left: 0%;
    padding-right: 0%;
    padding-left: -5px;
    padding-right: 6%;
  }
</style>
