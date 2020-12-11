
/*container_of(ptr, type, member)*/
/*作用：通过成员变量的地址得到它所在结构体的首地址*/
/*参数含义：*/
/*ptr -- member类型定义的指针变量*/
/*type -- 需要操作的数据类型,通常为结构体*/
/*member -- type结构的成员名称*/

#include <stdio.h>
#include <string.h>

#define offsetof(TYPE, MEMBER) ((size_t) &((TYPE *)0)->MEMBER)
#define container_of(ptr, type, member) ({                      \
        const typeof( ((type *)0)->member ) *__mptr = (ptr);    \
        (type *)( (char *)__mptr - offsetof(type,member) );})

typedef struct frame {
  int num;
  char name[32];
  float f1;
}frame_t;

int main(void)
{
  frame_t fra, *pf;
  fra.num = 1;
  fra.f1 = 1.23;
  memcpy(fra.name,"Hello",5);

  //通过成员变量的地址得到它所在结构体的首地址
  /*pf = container_of(&fra.num,frame_t,num);*/
  pf = container_of(&fra.name, frame_t, name);
  /*pf = container_of(&fra.f1,frame_t,f1);*/
  printf("pf->num = %d, pf->name = %s, pf->f1 = %f\n",pf->num, pf->name, pf->f1);

  return 0;
}

