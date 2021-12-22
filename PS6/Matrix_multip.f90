subroutine Matrix_multip(x,y,z)
                real(4)::x(5,3),y(3,5),z(5,5)
        !M * N
                z = MATMUL(x,y)

        end subroutine  Matrix_multip


