program Main
        implicit none

        integer::i,j,k,m,n,u
        real(4)::x(5,3),y(3,5),z(5,5)



        u=1
        open(u,file="/work/ese-xied/fortran_demo1/M.dat",status='old')

        do i=1,5
                read(u,*) (x(i,j),j=1,3)

        end do
        close(u)
        write(*,*)'M:'
        write(*,*)x(1,:)
        write(*,*)x(2,:)
        write(*,*)x(3,:)
        write(*,*)x(4,:)
        write(*,*)x(5,:)


         u=2
        open(u,file="/work/ese-xied/fortran_demo1/N.dat",status='old')

        do i=1,3
                read(u,*) (y(i,j),j=1,5)

        end do
        close(u)
        write(*,*)'N:'
        write(*,*)y(1,:)
        write(*,*)y(2,:)
        write(*,*)y(3,:)



        call Matrix_multip(x,y,z)
        write(*,*)'M*N:'
        do i=1,5
        write(*,'(f9.2)'),z(i,:)
        end do

end program Main

