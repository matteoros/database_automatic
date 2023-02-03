from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()


class Album(Base):
    __tablename__ = "albums"

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String(160))
    ArtistId = Column(ForeignKey('artists.ArtistId'), nullable=False)
    tracks = relationship("Track", backref="album")

    def __repr__(self):
        return "Album(AlbumId='%s', Title='%s', ArtistId='%s')" % (self.AlbumId, self.Title, self.ArtistId)


class Track(Base):
    __tablename__ = "tracks"

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String(200))
    AlbumId = Column(ForeignKey('albums.AlbumId'), nullable=True)

    def __repr__(self):
        return "Track(TrackId='%s', Name='%s', AlbumId='%s')" % (self.TrackId, self.Name, self.AlbumId)


class Artist(Base):
    __tablename__ = "artists"

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String(120))
    albums = relationship("Album", backref="artist")

    def __repr__(self):
        return "Artist(ArtistId='%s', Name='%s')" % (self.ArtistId, self.Name)
