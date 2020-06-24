"""initial migration

Revision ID: 494dc1460041
Revises: 
Create Date: 2020-06-22 13:49:49.709031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '494dc1460041'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flaskusers')
    op.drop_table('students')
    op.drop_table('books')
    op.drop_table('reviews')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('book', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('reviewer', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('review', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('review_detail', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['book'], ['books.id'], name='reviews_book_fkey'),
    sa.ForeignKeyConstraint(['reviewer'], ['users.id'], name='reviews_reviewer_fkey'),
    sa.PrimaryKeyConstraint('id', name='reviews_pkey')
    )
    op.create_table('books',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('isbn', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('author', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('year', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='books_pkey')
    )
    op.create_table('students',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('school', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='students_pkey')
    )
    op.create_table('flaskusers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='flaskusers_pkey')
    )
    # ### end Alembic commands ###
